from typing import Optional, List
from uuid import UUID
from domain.models.user import UserDomain
from sqlalchemy.orm import Session
from fastapi import HTTPException, status


class UserService:
    """
    Сервисный слой для работы с пользователями.
    """
    def __init__(self, db_session: Session):
        self.db_session = db_session
        self.user_domain = UserDomain(db_session)

    def create_user(self, username: str, email: str, hashed_password: str) -> UserDomain:
        """
        Создать нового пользователя.
        """
        try:
            return self.user_domain.create_user(username, email, hashed_password)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при создании пользователя: {str(e)}"
            )

    def get_user_by_id(self, user_id: UUID) -> Optional[UserDomain]:
        """
        Получить пользователя по ID.
        """
        user = self.user_domain.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Пользователь с таким ID не найден."
            )
        return user

    def deactivate_user(self, user_id: UUID) -> None:
        """
        Деактивировать пользователя.
        """
        try:
            self.user_domain.deactivate_user(user_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при деактивации пользователя: {str(e)}"
            )

    def delete_user(self, user_id: UUID) -> None:
        """
        Мягкое удаление пользователя.
        """
        try:
            self.user_domain.delete_user(user_id)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при удалении пользователя: {str(e)}"
            )

    def change_user_role(self, user_id: UUID, new_role: str) -> None:
        """
        Изменить роль пользователя.
        """
        try:
            self.user_domain.change_user_role(user_id, new_role)
        except ValueError as ve:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(ve)
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при изменении роли пользователя: {str(e)}"
            )

    def list_users(self) -> List[UserDomain]:
        """
        Получить список всех активных пользователей.
        """
        try:
            return self.user_domain.get_all_users()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ошибка при получении списка пользователей: {str(e)}"
            )
