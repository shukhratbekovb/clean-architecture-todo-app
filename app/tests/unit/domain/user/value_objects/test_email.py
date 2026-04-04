import pytest

from app.domain.user.value_objects.email.errors import InvalidEmailFormatError
from app.domain.user.value_objects.email.value_object import Email


@pytest.fixture
def valid_email() -> Email:
    return Email(value="test@domain.com")


@pytest.mark.parametrize(
    "value",
    [
        "user@gmail.com",
        "user.name@gmail.com",
        "user_name@gmail.com",
        "user-name@gmail.com",
        "user+tag@gmail.com",
        "user123@gmail.com",
        "123user@gmail.com",
        "user@mail.ru",
        "user@yandex.uz",
        "user@yahoo.com",
        "user@outlook.com",
        "user.name+tag@mail.ru",
        "user_123@yandex.com",
        "firstname.lastname@example.com",
        "user@subdomain.example.com",
        "user@example.co.uk",
        "USER@GMAIL.COM",
        "User.Name@Gmail.Com",
        "u@gmail.com",
        "user@example.travel",
    ]
)
def test_valid_email(value):
    assert Email(value=value).value == value.lower()


@pytest.mark.parametrize(
    "value",
    [
        "user@@gmail.com",
        "@gmail.com",
        "usergmail.com",
        "user@.com",
        "user@gmail.",
        "user@gmail.c",
        "user@",
        "@",
        "",
        "user @gmail.com",
        "user@ gmail.com",
        "user@gmail .com",
        ".user@gmail.com",
        "user.@gmail.com",
        "user@gmail..com",
        "user@-gmail.com",
        "user@gmail-.com",
        "user@.gmail.com",
        "user#name@gmail.com",
    ]
)
def test_invalid_email(value):
    with pytest.raises(InvalidEmailFormatError):
        Email(value=value)
