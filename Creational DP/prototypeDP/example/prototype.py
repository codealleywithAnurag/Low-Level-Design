from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        """Create a deep copy of the object."""
        pass
