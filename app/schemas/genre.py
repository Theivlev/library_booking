from pydantic import BaseModel
from typing import List, Optional # noqa


class GenreBase(BaseModel):
    """Базовая модель жанра"""
    name: str


class GenreCreate(GenreBase):
    """Модель для создания жанра"""
    pass
