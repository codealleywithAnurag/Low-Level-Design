from factory.factory import LaptopFactory
from factory.parts import Processor, RAM, Storage

class DellFactory(LaptopFactory):
    def create_processor(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return Processor("Intel i9")
            case 'business':
                return Processor("Intel i5")
            case _:
                return Processor("Intel i7")

    def create_ram(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return RAM("32GB")
            case 'business':
                return RAM("8GB")
            case _:
                return RAM("16GB")

    def create_storage(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return Storage("1TB SSD")
            case 'business':
                return Storage("512GB SSD")
            case _:
                return Storage("512GB SSD")
