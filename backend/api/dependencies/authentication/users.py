from typing import (
    TYPE_CHECKING,
    Annotated,
)

from fastapi import Depends

from core.models import (
    db_helper,
    User,
)

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

# TODO: вынести strategy.py auth.py access_token.py
async def get_users_db(
    session: Annotated[
        "AsyncSession",
        Depends(db_helper.session_getter),
    ],
):
    yield User.get_db(session=session)