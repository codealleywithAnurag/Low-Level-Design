from factory.factory import LaptopFactory
from factory.parts import Processor, RAM, Storage

class HPFactory(LaptopFactory):
    def create_processor(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return Processor("Intel i7")
            case 'business':
                return Processor("Intel i5")
            case 'standard':
                return Processor("Intel i3")
            case _:
                return Processor("Intel i3")
    def create_ram(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return RAM("16GB")
            case 'business':
                return RAM("8GB")
            case 'standard':
                return RAM("4GB")
            case _:
                return RAM("4GB")

    def create_storage(self, laptop_type):
        match laptop_type:
            case 'gaming':
                return Storage("1TB SSD")
            case 'business':
                return Storage("512GB SSD")
            case 'standard':
                return Storage("256GB SSD")
            case _:
                return Storage("256GB SSD")
