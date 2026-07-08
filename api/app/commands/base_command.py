from abc import ABC, abstractmethod


class BaseCommand(ABC):

    @abstractmethod
    def can_handle(self, user_id: str, message: str) -> bool:
        pass

    @abstractmethod
    def handle(self, user_id: str, message: str) -> str:
        pass