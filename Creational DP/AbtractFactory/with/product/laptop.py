class Laptop:
    def __init__(self, processor, ram, storage):
        self.processor = processor
        self.ram = ram
        self.storage = storage

    def display(self):
        print("Laptop Details:")
        print(f"Processor: {self.processor.get_details()}")
        print(f"RAM: {self.ram.get_details()}")
        print(f"Storage: {self.storage.get_details()}")
