import re
from dataclasses import dataclass

from app.domain.user.value_objects.email.errors import InvalidEmailFormatError

EMAIL_PATTERN = r"^[a-zA-Z0-9]([a-zA-Z0-9._+-]*[a-zA-Z0-9])?@[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]*[a-zA-Z0-9])?)*\.[a-zA-Z]{2,}$"


@dataclass(frozen=True)
class Email:
    """
    Value-Object Email нужен нам для электронных почт
    
    Attributes:
        value (str): Значение электронной почты
    """
    value: str

    def __post_init__(self):
        if not self.__validate():
            raise InvalidEmailFormatError()

        object.__setattr__(self, "value", self.value.lower())

    def __validate(self) -> bool:
        """
        Проводит Валидацию по указанному шаблону

        :return: Если совпадает то, возвращает True если нет то False
        """
        return bool(re.match(EMAIL_PATTERN, self.value))

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.value
