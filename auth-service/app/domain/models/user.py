from dataclasses import dataclass
from enum import Enum
from uuid import UUID, uuid4


# Перечисление ролей
class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


# Класс модели пользователя
@dataclass
class User:
    user_id: UUID
    username: str
    email: str
    hashed_password: str
    role: Role = Role.USER
    is_active: bool = True
    is_deleted: bool = False

    @staticmethod
    def create(username: str, email: str, hashed_password: str, role: Role = Role.USER) -> "User":
        # Проверки на валидность данных
        if not username or not email or not hashed_password:
            raise ValueError("Username, email, and hashed_password cannot be empty.")
        if "@" not in email:
            raise ValueError("Invalid email format.")
        
        try:
            return User(
                user_id=uuid4(),
                username=username,
                email=email,
                hashed_password=hashed_password,
                role=role,
                is_active=True,
                is_deleted=False
            )
        except Exception as e:
            raise RuntimeError(f"Failed to create user: {str(e)}")

    def deactivate(self):
        if not self.is_active:
            raise RuntimeError("User is already deactivated.")
        try:
            self.is_active = False
        except Exception as e:
            raise RuntimeError(f"Failed to deactivate user: {str(e)}")

    def soft_delete(self):
        if self.is_deleted:
            raise RuntimeError("User is already marked as deleted.")
        try:
            self.is_deleted = True
        except Exception as e:
            raise RuntimeError(f"Failed to soft delete user: {str(e)}")

    def change_role(self, new_role: Role):
        if new_role == self.role:
            raise RuntimeError(f"User already has the role: {new_role}.")
        try:
            self.role = new_role
        except Exception as e:
            raise RuntimeError(f"Failed to change role: {str(e)}")
