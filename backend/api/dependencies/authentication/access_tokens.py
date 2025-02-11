from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from core.models import (
    db_helper,
    AccessToken,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

# TODO: вынести strategy.py users.py access_token.py
async def get_access_tokens_db(
        session: Annotated[
            "AsyncSession",
            Depends(db_helper.session_getter),
        ],
):
    yield AccessToken.get_db(session=session)
