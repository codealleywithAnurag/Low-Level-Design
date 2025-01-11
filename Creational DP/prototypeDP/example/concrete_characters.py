from character import Character

class Warrior(Character):
    def __init__(self, name="Warrior", health=100, stamina=80, skills=None):
        super().__init__(name, health, stamina, skills or ["Sword Fighting"])

class Mage(Character):
    def __init__(self, name="Mage", health=70, stamina=50, skills=None):
        super().__init__(name, health, stamina, skills or ["Spell Casting"])

class Archer(Character):
    def __init__(self, name="Archer", health=80, stamina=60, skills=None):
        super().__init__(name, health, stamina, skills or ["Archery"])
