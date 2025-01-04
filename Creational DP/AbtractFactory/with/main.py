# main.py

from factory.dell_factory import DellFactory
from factory.hp_factory import HPFactory
from product.laptop import Laptop

def main():
    laptop_type = 'gaming' 

    dell_factory = DellFactory()

    dell_laptop = Laptop(
        processor=dell_factory.create_processor(laptop_type),
        ram=dell_factory.create_ram(laptop_type),
        storage=dell_factory.create_storage(laptop_type)
    )

    print(f"Dell {laptop_type.capitalize()} Laptop:")
    dell_laptop.display()
    print()

    hp_factory = HPFactory()

    hp_laptop = Laptop(
        processor=hp_factory.create_processor(laptop_type),
        ram=hp_factory.create_ram(laptop_type),
        storage=hp_factory.create_storage(laptop_type)
    )

    print(f"HP {laptop_type.capitalize()} Laptop:")
    hp_laptop.display()

if __name__ == "__main__":
    main()
