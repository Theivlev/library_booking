from fastapi import APIRouter

from app.api.endpoints import (
    user_router,
    booking_api_router)

main_router = APIRouter()
main_router.include_router(user_router)
main_router.include_router(
    booking_api_router, prefix='/bokings', tags=['Bookings']
)
