from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_cache.decorator import cache

from app.core.db import get_async_session
from app.core.user import current_user
from app.models import User
from app.schemas.booking import BookingRead, BookingCreate
from app.crud.booking import booking_crud

router = APIRouter()


@cache(expire=30)
@router.get("/active", response_model=list[BookingRead])
async def get_bookings(session: AsyncSession = Depends(get_async_session)):
    return await booking_crud.get_active_bookings(session)


@cache(expire=30)
@router.get("/{booking_id}", response_model=BookingRead)
async def fetch_booking(booking_id: int,
                        session: AsyncSession = Depends(get_async_session)):
    booking = await booking_crud.get_booking_by_book_id(booking_id)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Бронь не обнаружена"
            )

    return booking


@router.post("", response_model=BookingRead)
async def create_active_booking(booking: BookingCreate,
                                session: AsyncSession = Depends
                                (get_async_session),
                                current_user: User = Depends(current_user)):

    existing_booking = await booking_crud.get_booking_by_book_id(
        session, booking.book_id)
    if existing_booking:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Книга уже забронирована")

    return await booking_crud.create_booking(
        session,
        user_id=current_user.id,
        **booking.dict()
        )


@router.delete("/{booking_id}", response_model=dict)
async def delete_active_booking(booking_id: int,
                                session: AsyncSession = Depends
                                (get_async_session),
                                current_user: User = Depends(current_user)):
    booking = await booking_crud.get_booking_by_book_id(session, booking_id)
    if booking and booking.user_id == current_user.id:
        return await booking_crud.delete_booking(session, booking_id)
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Бронь не найдена или вы пытаетесь удалить не свою бронь")
