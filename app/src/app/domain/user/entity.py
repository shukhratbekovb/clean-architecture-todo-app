import uuid
from dataclasses import dataclass, field
from datetime import datetime

from app.domain.user.value_objects.email.value_object import Email
from app.domain.user.value_objects.name.value_object import Name


@dataclass
class User:
    id: uuid.UUID
    email: Email
    first_name: Name
    last_name: Name
    password_hash: str
    is_active: bool = field(default=True)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create(
            cls,
            id: uuid.UUID,
            email: str,
            first_name: str,
            last_name: str,
            password_hash: str,
    ):
        return cls(
            id=id,
            email=Email(email),
            first_name=Name(first_name),
            last_name=Name(last_name),
            password_hash=password_hash,
        )

    def _touch(self):
        self.updated_at = datetime.now()

    def change_email(self, new_email: Email):
        self.email = new_email
        self._touch()

    def change_name(self, first_name: Name, last_name: Name):
        self.first_name = first_name
        self.last_name = last_name
        self._touch()

    def __eq__(self, other) -> bool:
        if not isinstance(other, User):
            raise
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)
