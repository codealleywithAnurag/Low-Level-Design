from parts.processor import Processor
from parts.ram import RAM
from parts.storage import Storage

class DellFactory:
    def create_processor(self, laptop_type):
        if laptop_type == 'gaming':
            return Processor("Intel i9")
        elif laptop_type == 'business':
            return Processor("Intel i5")
        else:
            return Processor("Intel i7")

    def create_ram(self, laptop_type):
        if laptop_type == 'gaming':
            return RAM("32GB")
        elif laptop_type == 'business':
            return RAM("8GB")
        else:
            return RAM("16GB")

    def create_storage(self, laptop_type):
        if laptop_type == 'gaming':
            return Storage("1TB SSD")
        elif laptop_type == 'business':
            return Storage("512GB SSD")
        else:
            return Storage("512GB SSD")
