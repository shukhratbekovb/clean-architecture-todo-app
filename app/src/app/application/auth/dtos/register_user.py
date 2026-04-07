from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class RegisterUserCommand:
    email: str
    first_name: str
    last_name: str
    password: str

@dataclass(frozen=True)
class RegisterUserResult:
    user_id: UUID