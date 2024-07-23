from sqlalchemy import Column, DateTime, Integer, ForeignKey

from app.core.db import Base


class Booking(Base):
    user_id = Column(Integer, ForeignKey("user.id"))
    book_id = Column(Integer, ForeignKey("book.id"))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
