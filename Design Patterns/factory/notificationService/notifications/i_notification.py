from abc import ABC, abstractmethod

class INotification(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass
