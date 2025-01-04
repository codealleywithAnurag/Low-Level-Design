from product.laptop_part import LaptopPart

class Processor(LaptopPart):
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return self.name

class RAM(LaptopPart):
    def __init__(self, size):
        self.size = size

    def get_details(self):
        return self.size

class Storage(LaptopPart):
    def __init__(self, capacity):
        self.capacity = capacity

    def get_details(self):
        return self.capacity
