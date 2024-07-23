from pydantic import BaseModel
from typing import List, Optional # noqa


class BookBase(BaseModel):
    """Базовая модель книги"""
    title: str
    cost: float
    num_pages: int
    author: str


class BookCreate(BookBase):
    """Модель для создания книги"""
    pass


class BookGenreBase(BaseModel):
    """Базовая модель связи книги и жанра"""
    book_id: int
    genre_id: int


class BookGenreCreate(BookGenreBase):
    """Модель для создания связи книги и жанра"""
    pass
