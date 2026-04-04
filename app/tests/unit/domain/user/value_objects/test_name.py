import pytest

from app.domain.user.value_objects.name.errors import InvalidNameLengthError
from app.domain.user.value_objects.name.value_object import Name


@pytest.fixture
def valid_name() -> Name:
    return Name("Test")


@pytest.mark.parametrize(
    "value",
    [
        "Ramiz",
        "Bobur"
    ]
)
def test_valid_name(value):
    assert Name(value=value).value == value


@pytest.mark.parametrize(
    "value",
    [
        "A",
        "a",
        "a" * 512
    ]
)
def test_invalid_name(value):
    with pytest.raises(InvalidNameLengthError):
        Name(value=value)
