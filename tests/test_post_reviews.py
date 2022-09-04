import json
from unittest.mock import Mock, patch

from app.main import app
from fastapi.testclient import TestClient
from requests.exceptions import HTTPError

client = TestClient(app)


def book_42():
    return {
        'count':
        1,
        'next':
        None,
        'previous':
        None,
        'results': [{
            'id':
            42,
            'title':
            'The Strange Case of Dr. Jekyll and Mr. Hyde',
            'authors': [{
                'name': 'Stevenson, Robert Louis',
                'birth_year': 1850,
                'death_year': 1894
            }],
            'translators': [],
            'subjects': [
                'Horror tales', 'London (England) -- Fiction',
                'Multiple personality -- Fiction', 'Physicians -- Fiction',
                'Psychological fiction', 'Science fiction',
                'Self-experimentation in medicine -- Fiction'
            ],
            'bookshelves': [
                'Gothic Fiction', 'Horror', 'Movie Books',
                'Precursors of Science Fiction'
            ],
            'languages': ['en'],
            'copyright':
            False,
            'media_type':
            'Text',
            'formats': {
                'text/plain; charset=us-ascii':
                'https://www.gutenberg.org/files/42/42-0.txt',
                'application/epub+zip':
                'https://www.gutenberg.org/ebooks/42.epub.images',
                'application/rdf+xml':
                'https://www.gutenberg.org/ebooks/42.rdf',
                'text/plain':
                'https://www.gutenberg.org/ebooks/42.txt.utf-8',
                'application/x-mobipocket-ebook':
                'https://www.gutenberg.org/ebooks/42.kindle.images',
                'text/html':
                'https://www.gutenberg.org/files/42/42-h/42-h.htm',
                'application/octet-stream':
                'https://www.gutenberg.org/files/42/42-0.zip',
                'image/jpeg':
                'https://www.gutenberg.org/cache/epub/42/pg42.cover.medium.jpg'
            },
            'download_count':
            1149
        }]
    }


@patch('requests.get')
def test_post_review_book(requests_mock, create_mongo_connection):
    review = {'book_id': 42, 'rating': 5, 'review': 'Test Reviews'}
    review = json.dumps(review)

    success_response = Mock()
    success_response.json.return_value = book_42()
    success_response.raise_for_status.side_effect = None
    requests_mock.return_value = success_response

    response = client.post('/books/review', data=review)

    assert response.status_code == 200
    assert response.json() == {
        'id':
        42,
        'title':
        'The Strange Case of Dr. Jekyll and Mr. Hyde',
        'authors': [{
            'name': 'Stevenson, Robert Louis',
            'birth_year': 1850,
            'death_year': 1894
        }],
        'languages': ['en'],
        'download_count':
        1149,
        'reviews': [{
            'rating': 5,
            'review': 'Test Reviews'
        }],
        'average_rating':
        5.0
    }


@patch('requests.get')
def test_post_two_reviews(requests_mock, create_mongo_connection):
    review = {'book_id': 42, 'rating': 5, 'review': 'Test Reviews'}
    review = json.dumps(review)

    success_response = Mock()
    success_response.json.return_value = book_42()
    success_response.raise_for_status.side_effect = None
    requests_mock.return_value = success_response

    client.post('/books/review', data=review)

    review = {'book_id': 42, 'rating': 4, 'review': 'Test Reviews'}
    review = json.dumps(review)
    response = client.post('/books/review', data=review)

    assert response.status_code == 200
    assert response.json() == {
        'id':
        42,
        'title':
        'The Strange Case of Dr. Jekyll and Mr. Hyde',
        'authors': [{
            'name': 'Stevenson, Robert Louis',
            'birth_year': 1850,
            'death_year': 1894
        }],
        'languages': ['en'],
        'download_count':
        1149,
        'reviews': [{
            'rating': 5,
            'review': 'Test Reviews'
        }, {
            'rating': 4,
            'review': 'Test Reviews'
        }],
        'average_rating':
        4.5
    }


def test_post_invalid_review():
    review = {'book_id': 42, 'rating': 'A', 'review': 'Test Reviews'}
    review = json.dumps(review)
    response = client.post('/books/review', data=review)
    assert response.status_code == 422
    assert response.json() == {
        'detail': [{
            'loc': ['body', 'rating'],
            'msg': 'value is not a valid integer',
            'type': 'type_error.integer'
        }]
    }


@patch('requests.get')
def test_post_review_http_error(requests_mock):
    review = {'book_id': 42, 'rating': 5, 'review': 'Test Reviews'}
    review = json.dumps(review)

    fail_response = Mock()
    fail_response.status_code = 500
    fail_response.raise_for_status.side_effect = HTTPError(
        'Gutendex not working')
    requests_mock.return_value = fail_response
    response = client.post('/books/review', data=review)
    assert response.status_code == 500
    assert response.json() == {'message': 'Gutendex not working'}


@patch('requests.get')
def test_post_review_book_not_found(requests_mock):
    review = {'book_id': 42, 'rating': 5, 'review': 'Test Reviews'}
    review = json.dumps(review)

    fail_response = Mock()
    fail_response.status_code = 200
    fail_response.json.return_value = {
        'count': 0,
        'next': None,
        'previous': None,
        'results': []
    }

    requests_mock.return_value = fail_response
    response = client.post('/books/review?book_id=800000', data=review)
    assert response.status_code == 404
    assert response.json() == {'message': 'Book not found'}
