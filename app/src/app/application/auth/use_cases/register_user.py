import uuid

from app.application.auth.dtos.register_user import RegisterUserCommand, RegisterUserResult
from app.application.auth.interfaces.password_hasher import PasswordHasher
from app.application.shared.uow import UnitOfWork
from app.domain.shared.specification import Specification

from app.domain.user.entity import User


class RegisterUserUseCase:
    def __init__(
            self,
            uow: UnitOfWork,
            hasher: PasswordHasher,
            password_spec: Specification[str]
    ):
        self.uow = uow
        self.hasher = hasher
        self.password_spec = password_spec

    async def execute(
            self,
            cmd: RegisterUserCommand
    ) -> RegisterUserResult:
        async with self.uow:
            exists = await self.uow.users.exists_email(cmd.email)
            if exists:
                raise

            # Проверка Пароля
            if self.password_spec.is_satisfied_by(cmd.password):
                raise

            hashed_password = self.hasher.hash(cmd.password)

            user_id = uuid.uuid4()

            user = User.create(
                id=user_id,
                email=cmd.email,
                first_name=cmd.first_name,
                last_name=cmd.last_name,
                password_hash=hashed_password
            )

            user = await self.uow.users.create_user(user)

            await self.uow.commit()

            return RegisterUserResult(user_id=user.id)
