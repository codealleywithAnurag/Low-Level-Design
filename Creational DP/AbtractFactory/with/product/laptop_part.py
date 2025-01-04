from abc import ABC, abstractmethod

class LaptopPart(ABC):
    @abstractmethod
    def get_details(self):
        pass
