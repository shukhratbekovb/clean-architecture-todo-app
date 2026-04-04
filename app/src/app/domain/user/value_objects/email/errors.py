from app.domain.shared.errors import DomainError


class EmailError(DomainError):
    """
    Базовая Ошибка Email VO
    """


class InvalidEmailFormatError(EmailError):
    """
    Ошибка Неправильного Формата Email
    """
