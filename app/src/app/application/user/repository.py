from typing import Protocol

from app.domain.user.entity import User


class UserRepository(Protocol):
    async def exists_email(self, email: str) -> bool: ...

    async def create_user(self, user: User) -> User: ...
