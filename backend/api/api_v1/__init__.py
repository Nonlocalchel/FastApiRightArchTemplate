from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from core.config import settings
from .auth import router as users_router
from .posts import router as posts_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(
    users_router
)