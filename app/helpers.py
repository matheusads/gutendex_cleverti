import json
from decimal import Decimal
from math import ceil
from typing import List, Optional, Tuple

import requests
from app.database.models import Books
from app.models import (BookModel, GetBooksResponse, PaginationOutput,
                        ReviewModel, ReviewModelInput)


class NotFoundBook(Exception):
    pass


def get_pagination_output(page: int, count: int,
                          page_size: int) -> PaginationOutput | None:
    if count:
        return PaginationOutput(count=count,
                                page=page,
                                page_size=page_size,
                                pages=get_page_count(page_size, count))
    return PaginationOutput()


def get_page_count(page_size: int, count: int = 1) -> int:
    return ceil(count / page_size)


def request_books(book_id: Optional[int] = None,
                  page: Optional[int] = 1,
                  title: Optional[str] = None) -> GetBooksResponse:
    gutendex_api = f'https://gutendex.com/books/?page={page}'

    if book_id:
        gutendex_api = f'{gutendex_api}&ids={book_id}'

    if title:
        gutendex_api = f'{gutendex_api}&search={title}'

    response = requests.get(gutendex_api)
    response.raise_for_status()

    response_data = response.json()
    count = response_data.get('count')
    books = response_data.get('results')
    if not books:
        raise NotFoundBook('Book not found')

    pagination = get_pagination_output(page, count, len(books))
    for book in books:
        book['reviews'], book[
            'average_rating'] = get_reviews_and_average_rating(book.get('id'))

    return GetBooksResponse(pagination=pagination, books=books)


def get_reviews_and_average_rating(
        book_id: int) -> Tuple[List[ReviewModel], Decimal] | Tuple[None, None]:

    book = Books.objects(id=book_id).only('reviews', 'average_rating').first()
    if book:
        reviews: List[ReviewModel] = [
            json.loads(r.to_json()) for r in book.reviews
        ]
        return reviews, book.average_rating
    return None, None


def insert_or_update_book(book: BookModel,
                          review: ReviewModelInput) -> BookModel:
    book_db = Books.objects(id=book.id).first()
    if not book_db:
        book_db = Books(**book.dict()).save()

    new_avg = review.rating
    if book.reviews:
        new_avg = (len(book.reviews) * book.average_rating +
                   review.rating) / (len(book.reviews) + 1)

    book_db.update(push__reviews=review.dict(exclude={'book_id'}),
                   average_rating=new_avg,
                   upsert=True)
    book_db = book_db.reload()
    book_data = json.loads(book_db.to_json())

    return BookModel(**book_data, id=book_data.get('_id'))


def get_best_n_books(top_books: int) -> List[BookModel] | List:
    result = []
    books = Books.objects().order_by('-average_rating').limit(top_books)

    if books:
        for book in books:
            book_data = json.loads(book.to_json())
            result.append(BookModel(**book_data, id=book_data.get('_id')))
    return result
