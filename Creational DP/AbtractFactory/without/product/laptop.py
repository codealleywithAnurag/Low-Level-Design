class Laptop:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display(self):
        print(f"{self.processor}\n{self.ram}\n{self.storage}")
