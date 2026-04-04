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
