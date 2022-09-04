from http import HTTPStatus
from typing import Optional, List

from pydantic.types import conint

from app.events import on_application_shutdown, on_application_startup
from app.helpers import NotFoundBook, insert_or_update_book, request_books, get_best_n_books
from app.models import (BookModel, ErrorResponse, GetBooksResponse,
                        ReviewModelInput)
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from requests import HTTPError

app = FastAPI()

app.add_event_handler("startup", on_application_startup)
app.add_event_handler("shutdown", on_application_shutdown)

GUTENDEX_API = 'https://gutendex.com/books'

responses = {
    404: {
        "model": ErrorResponse,
        "description": "Item not found"
    },
    412: {
        "model": ErrorResponse,
        "description": "Validation error"
    },
    500: {
        "model": ErrorResponse,
        "description": "Unexpected error"
    },
}


@app.get("/books/",
         response_model=GetBooksResponse,
         responses=responses,
         response_model_exclude_unset=True)
def get_books(book_id: Optional[int] = None,
              title: Optional[str] = None,
              page: Optional[int] = 1):
    try:
        return request_books(book_id=book_id, page=page, title=title)
    except NotFoundBook as not_found_error:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND,
                            content={"message": str(not_found_error)})
    except HTTPError as error:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": str(error)})
    except ValidationError as error:
        return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            content={"message": str(error)})
    except Exception:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": "Unexpected internal error"})


@app.post('/books/review', response_model=BookModel, responses=responses)
def post_review(review: ReviewModelInput):
    try:
        result: GetBooksResponse = request_books(review.book_id)
        book: BookModel = result.books[0]
        return insert_or_update_book(book, review)

    except NotFoundBook as not_found_error:
        return JSONResponse(status_code=HTTPStatus.NOT_FOUND,
                            content={"message": str(not_found_error)})
    except HTTPError as error:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": str(error)})
    except ValidationError as error:
        return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            content={"message": str(error)})
    except Exception:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": "Unexpected internal error"})


@app.get('/books/ranking', response_model=List[BookModel])
def get_best_books(top_books: conint(ge=1)):
    try:
        return get_best_n_books(top_books)
    except ValidationError as error:
        return JSONResponse(status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                            content={"message": str(error)})
    except Exception:
        return JSONResponse(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            content={"message": "Unexpected internal error"})
