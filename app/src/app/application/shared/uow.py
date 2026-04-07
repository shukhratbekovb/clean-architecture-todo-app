from typing import Protocol

from app.application.user.repository import UserRepository


class UnitOfWork(Protocol):
    users: UserRepository

    async def commit(self): ...

    async def rollback(self): ...

    async def __aenter__(self): ...

    async def __aexit__(self, exc_type, exc_val, exc_tb): ...
