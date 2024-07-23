from pydantic import BaseSettings


class Settings(BaseSettings):
    """Класс для работы с переменными окружения."""
    app_title: str = 'Борьба за книги'
    description: str = 'Пользователи бронируют книги'
    secret: str = 'SECRET'
    database_url_lite: str = "sqlite+aiosqlite:///./fastapi.db"

    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def DATABASE_URL(self):
        return (f'postgresql+asyncpg://{self.POSTGRES_USER}:'
                f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
                f'{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}')

    class Config:
        env_file = '.env'


settings = Settings()
