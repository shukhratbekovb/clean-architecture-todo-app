from app.domain.shared.errors import DomainError


class NameVOError(DomainError):
    """
    Базовая ошибка Name
    """

class InvalidNameLengthError(NameVOError):
    """
    Ошибка длины имени
    """

# Domain -> Name -> Конкретная Ошибка