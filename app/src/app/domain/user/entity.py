import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: uuid.UUID | None
    email: str  # Email
    first_name: str  # Name
    last_name: str  # Name
    password_hash: str
    is_active: bool = field(default=True)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
