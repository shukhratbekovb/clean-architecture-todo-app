from dataclasses import dataclass

from app.domain.user.value_objects.name.errors import InvalidNameLengthError


@dataclass(frozen=True)
class Name:
    """
    Value Object Name нужен для имен

    Attributes:
        value(str): Значение имени
    """
    value: str

    def __post_init__(self):
        if not self.__validate():
            raise InvalidNameLengthError()

    # От 3 до 255
    def __validate(self) -> bool:
        return 255 >= len(self.value) >= 3

    def __str__(self) -> str:
        return self.value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, Name):
            return self.value == other.value
        if isinstance(other, str):
            return self.value == other
        raise
