from app.domain.shared.specification import Specification, T


class HasUpperLetterPasswordSpecification(Specification[str]):
    def is_satisfied_by(self, password: str) -> bool:
        return any(c.isupper() for c in password)


class HasLowerLetterPasswordSpecification(Specification[str]):
    def is_satisfied_by(self, password: str) -> bool:
        return any(c.islower() for c in password)


class HasDigitPasswordSpecification(Specification[str]):
    def is_satisfied_by(self, password: str) -> bool:
        return any(c.isdigit() for c in password)


class HasSpecialCharacterPasswordSpecification(Specification[str]):
    SPECIAL = set("!@#$%^&*()-_+=/{}[];:'\"\\|`~?,. ")

    def is_satisfied_by(self, password: str) -> bool:
        return any(c in self.SPECIAL for c in password)


class LengthPasswordSpecification(Specification[str]):
    def is_satisfied_by(self, password: str) -> bool:
        return len(password) >= 8
