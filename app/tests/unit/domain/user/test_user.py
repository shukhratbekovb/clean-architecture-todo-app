import uuid
from uuid import UUID

import pytest

from app.domain.shared.errors import DomainError
from app.domain.user.entity import User
from app.domain.user.value_objects.email.value_object import Email
from app.domain.user.value_objects.name.value_object import Name

from tests.unit.domain.user.value_objects.test_email import valid_email
from tests.unit.domain.user.value_objects.test_name import valid_name


@pytest.fixture
def user_id() -> UUID:
    return uuid.uuid4()


@pytest.fixture
def hashed_password() -> str:
    return "hashed_password"


@pytest.fixture
def valid_user(user_id, valid_email, valid_name, hashed_password) -> User:
    return User(
        id=user_id,
        email=valid_email,
        first_name=valid_name,
        last_name=valid_name,
        password_hash=hashed_password
    )


@pytest.mark.parametrize(
    "email, first_name, last_name",
    [
        ("ramiz@gmail.com", "Ramiz", "Ram"),
        ("shukhratbekovb@gmail.com", "Bobur", "Shuhratbekov")
    ]
)
def test_create_user(user_id, hashed_password, email, first_name, last_name):
    user = User.create(
        id=user_id,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password_hash=hashed_password
    )
    assert user.id == user_id
    assert user.password_hash == hashed_password
    assert user.email == email
    assert user.first_name == first_name
    assert user.last_name == last_name


@pytest.mark.parametrize(
    "email, first_name, last_name",
    [
        ("ramiz", "Ramiz", "Ram"),
        ("ramiz@gmail.com", "Ra", "Ram"),
        ("ramiz@gmail.com", "Ramiz", "Ra"),
    ]
)
def test_invalid_create_user(user_id, hashed_password, email, first_name, last_name):
    with pytest.raises(DomainError):
        User.create(
            id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password_hash=hashed_password
        )


def test_user_fullname(valid_user):
    assert valid_user.full_name == f"{valid_user.first_name} {valid_user.last_name}"


def test_change_email(valid_user: User, valid_email: Email):
    last_update = valid_user.updated_at
    valid_user.change_email(valid_email)
    assert valid_user.email == valid_email
    assert last_update != valid_user.updated_at


def test_change_name(valid_user: User, valid_name: Name):
    last_update = valid_user.updated_at
    valid_user.change_name(valid_name, valid_name)
    assert valid_user.first_name == valid_name
    assert valid_user.last_name == valid_name
    assert last_update != valid_user.updated_at
