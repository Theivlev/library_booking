from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.booking import Booking

from datetime import datetime


class CRUDBookings:
    async def create_booking(
            self,
            session: AsyncSession,
            user_id: int,
            book_id: int,
            start_date: datetime,
            end_date: datetime,
            ):
        """Создание бронирования книги пользователем"""
        new_booking = Booking(
            user_id=user_id,
            book_id=book_id,
            start_date=start_date,
            end_date=end_date,
            is_booked=True,
            )
        session.add(new_booking)
        await session.commit()
        return new_booking

    async def get_active_bookings(self, session: AsyncSession):
        """Получение списка активных бронирований"""
        query = select(Booking).where(Booking.end_date > datetime.now())
        result = await session.execute(query)
        return result.scalars().all()

    async def get_booking_by_book_id(self,
                                     session: AsyncSession, book_id: int):
        """Получение одного бронирования по book_id"""
        query = select(Booking).where(Booking.book_id == book_id)
        result = await session.execute(query)
        booking = result.scalar()
        return booking

    async def delete_booking(self, session: AsyncSession, booking_id: int):
        """Удаление бронирования"""
        booking = await session.get(Booking, booking_id)
        if booking:
            session.delete(booking)
            await session.commit()
        else:
            return None


booking_crud = CRUDBookings()
