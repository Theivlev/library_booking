from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    """Модель чтения пользователя"""
    pass


class UserCreate(schemas.BaseUserCreate):
    """Модель создания пользователя"""
    pass


class UserUpdate(schemas.BaseUserUpdate):
    """Модель обновления пользователя"""
    pass
