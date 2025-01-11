from prototype_manager import PrototypeManager
from concrete_characters import Warrior, Mage, Archer

def main():
    # Initialize Prototype Manager
    manager = PrototypeManager()

    # Register prototypes
    manager.addPrototype("warrior", Warrior())
    manager.addPrototype("mage", Mage())
    manager.addPrototype("archer", Archer())

    # Clone and customize characters
    warrior1 = manager.getPrototype("warrior")
    warrior1.name = "Thorin"
    warrior1.skills.append("Shield Bash")

    mage1 = manager.getPrototype("mage")
    mage1.name = "Gandalf"
    mage1.skills.append("Lightning Strike")

    archer1 = manager.getPrototype("archer")
    archer1.name = "Legolas"
    archer1.stamina += 10
    archer1.skills.append("Rapid Shot")

    # Print customized characters
    print(warrior1)
    print(mage1)
    print(archer1)

    # Print original prototypes to verify no changes
    print("\nOriginal Prototypes:")
    print(manager.getPrototype("warrior"))
    print(manager.getPrototype("mage"))
    print(manager.getPrototype("archer"))

if __name__ == "__main__":
    main()
