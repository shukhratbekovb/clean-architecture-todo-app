import pytest

from app.domain.user.specifications.password import (
    HasUpperLetterPasswordSpecification,
    HasLowerLetterPasswordSpecification,
    HasDigitPasswordSpecification,
    HasSpecialCharacterPasswordSpecification,
    LengthPasswordSpecification
)


@pytest.fixture
def upper_spec():
    return HasUpperLetterPasswordSpecification()


@pytest.fixture
def lower_spec():
    return HasLowerLetterPasswordSpecification()


@pytest.fixture
def digit_spec():
    return HasDigitPasswordSpecification()


@pytest.fixture
def special_char_spec():
    return HasSpecialCharacterPasswordSpecification()


@pytest.fixture
def length_spec():
    return LengthPasswordSpecification()


@pytest.fixture
def password_spec(
        upper_spec: HasUpperLetterPasswordSpecification,
        lower_spec: HasLowerLetterPasswordSpecification,
        digit_spec: HasDigitPasswordSpecification,
        special_char_spec: HasSpecialCharacterPasswordSpecification,
        length_spec: LengthPasswordSpecification
):
    return upper_spec & lower_spec & digit_spec & special_char_spec & length_spec


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", False),
        ("Ramiz", True),
    ]
)
def test_has_upper_password_specification(
        upper_spec: HasUpperLetterPasswordSpecification,
        password: str,
        expected: bool
):
    assert upper_spec.is_satisfied_by(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", True),
        ("Ramiz", True),
        ("RAMIZ", False)
    ]
)
def test_has_lower_password_specification(
        lower_spec: HasLowerLetterPasswordSpecification,
        password: str,
        expected: bool
):
    assert lower_spec.is_satisfied_by(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", False),
        ("Ramiz", False),
        ("ra123", True),
    ]
)
def test_has_digit_password_specification(
        digit_spec: HasDigitPasswordSpecification,
        password: str,
        expected: bool
):
    assert digit_spec.is_satisfied_by(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", False),
        ("Ramiz", False),
        ("ra123", False),
        ("ra@123", True),
    ]
)
def test_has_special_character_password_specification(
        special_char_spec: HasSpecialCharacterPasswordSpecification,
        password: str,
        expected: bool
):
    assert special_char_spec.is_satisfied_by(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", False),
        ("Ramiz", False),
        ("ra123", False),
        ("ra@123", False),
        ("RamizRam", True),
    ]
)
def test_length_password_specification(
        length_spec: LengthPasswordSpecification,
        password: str,
        expected: bool
):
    assert length_spec.is_satisfied_by(password) == expected


@pytest.mark.parametrize(
    "password, expected",
    [
        ("ramiz", False),
        ("Ramiz", False),
        ("ra123", False),
        ("ra@123", False),
        ("Ra@123", False),
        ("Ramiz@1234", True)
    ]
)
def test_password_specification(
        password_spec,
        password: str,
        expected: bool
):
    assert password_spec.is_satisfied_by(password) == expected
