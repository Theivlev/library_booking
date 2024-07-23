"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base  # noqa
from app.models import User  # noqa
from app.models.book import Book, Author, Genre, BookGenre # noqa
from app.models.booking import Booking # noqa
