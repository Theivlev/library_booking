from fastapi import FastAPI
from app.api.routers import main_router
from app.core.config import settings

from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware


limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])

app = FastAPI(title=settings.app_title)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(main_router)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="tasks-cache")
