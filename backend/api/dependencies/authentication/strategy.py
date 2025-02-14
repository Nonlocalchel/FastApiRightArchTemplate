from typing import (
    TYPE_CHECKING,
    Annotated,
)
from fastapi import Depends
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)

from api.dependencies.authentication.access_tokens import get_access_tokens_db
from core.config import settings

if TYPE_CHECKING:
    from core.models import AccessToken


# TODO: вынести strategy.py auth.py access_token.py
def get_database_strategy(
        access_token_db: Annotated[
            AccessTokenDatabase["AccessToken"],
            Depends(get_access_tokens_db),
        ],
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )
