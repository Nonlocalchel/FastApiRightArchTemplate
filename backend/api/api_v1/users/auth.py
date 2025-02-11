from fastapi import APIRouter

from .fastapi_users_router import fastapi_users
from api.dependencies.authentication import authentication_backend
from core.config import settings
from core.schemas.users import (
    UserRead,
    UserCreate,
)

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        authentication_backend,
        # requires_verification=True,
    ),
)
