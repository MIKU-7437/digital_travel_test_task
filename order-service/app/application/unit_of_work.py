from abc import ABC, abstractmethod

class IUnitOfWork(ABC):
    @abstractmethod
    def commit(self) -> None:
        """Сохранить все изменения в рамках транзакции."""
        pass

    @abstractmethod
    def rollback(self) -> None:
        """Откатить изменения в рамках транзакции."""
        pass

    @abstractmethod
    def __enter__(self) -> "IUnitOfWork":
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass
