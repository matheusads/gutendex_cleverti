from decimal import Decimal
from typing import List, Optional

from pydantic import BaseModel, conint
from pydantic.fields import Field


class ReviewModel(BaseModel):
    rating: conint(ge=0, le=5)
    review: str


class ReviewModelInput(ReviewModel):
    book_id: int


class AuthorModel(BaseModel):
    name: str
    birth_year: Optional[int]
    death_year: Optional[int]


class BookModel(BaseModel):
    id: int
    title: str
    authors: Optional[List[AuthorModel]]
    languages: List[str]
    download_count: Optional[int]
    reviews: Optional[List[ReviewModel]] = Field(default_factory=list)
    average_rating: Optional[Decimal]


class PaginationOutput(BaseModel):
    page: Optional[conint(ge=1)]
    count: Optional[conint(ge=0)]
    pages: Optional[conint(ge=0)]
    page_size: Optional[conint(ge=0)]


class GetBooksResponse(BaseModel):
    pagination: Optional[PaginationOutput]
    books: Optional[List[BookModel]]


class ErrorResponse(BaseModel):
    message: str
