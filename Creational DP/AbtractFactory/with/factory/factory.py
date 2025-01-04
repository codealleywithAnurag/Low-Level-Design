from abc import ABC, abstractmethod
from product.laptop_part import LaptopPart

class LaptopFactory(ABC):
    @abstractmethod
    def create_processor(self) -> LaptopPart:
        pass

    @abstractmethod
    def create_ram(self) -> LaptopPart:
        pass

    @abstractmethod
    def create_storage(self) -> LaptopPart:
        pass
