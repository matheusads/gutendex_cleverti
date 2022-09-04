from app.database.models import Books
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def insert_books():
    for i in range(10):
        Books(id=i, title=f'Test Book {i}', languages=['en'],
              average_rating=i).save()


def test_best_3_books():
    insert_books()

    response = client.get('/books/ranking?top_books=3')
    assert response.status_code == 200
    assert response.json() == [{
        'id': 9,
        'title': 'Test Book 9',
        'authors': [],
        'languages': ['en'],
        'download_count': None,
        'reviews': [],
        'average_rating': 9.0
    }, {
        'id': 8,
        'title': 'Test Book 8',
        'authors': [],
        'languages': ['en'],
        'download_count': None,
        'reviews': [],
        'average_rating': 8.0
    }, {
        'id': 7,
        'title': 'Test Book 7',
        'authors': [],
        'languages': ['en'],
        'download_count': None,
        'reviews': [],
        'average_rating': 7.0
    }]


def test_top_books_invalid():
    response = client.get('/books/ranking?top_books=x')
    assert response.status_code == 422