from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class Book(Base):
    """Модель записи"""
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String, index=True)
    cost = Column(Float)
    num_pages = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'), unique=True)
    author = relationship('Author', backref='book', uselist=False)


class Author(Base):
    name = Column(String)


class Genre(Base):
    name = Column(String, unique=True, index=True)


class BookGenre(Base):
    book_id = Column(Integer, ForeignKey('book.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genre.id'), primary_key=True)
    book = relationship("Book", backref="book_genre")
    genre = relationship("Genre", backref="genre_book")
