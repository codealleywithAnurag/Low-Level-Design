from copy import deepcopy
from prototype import Prototype

class Character(Prototype):
    def __init__(self, name, health, stamina, skills=None):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.skills = skills if skills else []

    def clone(self):
        """Clone the character object using deepcopy."""
        return deepcopy(self)

    def __str__(self):
        """String representation of the character."""
        return (f"Name: {self.name}, Health: {self.health}, "
                f"Stamina: {self.stamina}, Skills: {self.skills}")
