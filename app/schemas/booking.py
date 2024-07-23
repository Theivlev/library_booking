from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BookingBase(BaseModel):
    book_id: int
    start_date: datetime
    end_date: datetime

    class Config:
        orm_mode = True


class BookingRead(BookingBase):
    id: int


class BookingCreate(BaseModel):
    book_id: int
    start_date: datetime
    end_date: datetime


class BookingUpdate(BaseModel):
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
