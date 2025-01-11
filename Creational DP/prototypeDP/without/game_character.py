class Character:
    def __init__(self, health, stamina, skills):
        self.health = health
        self.stamina = stamina
        self.skills = skills

def main():
    warrior = Character(health=100, stamina=50, skills=["Swordsmanship", "Shield Block"])

    warrior2 = Character(
        health=warrior.health,
        stamina=warrior.stamina,
        skills=list(warrior.skills),
    )
    warrior2.skills.append("Battle Cry")

    print(f"Warrior 1: Health={warrior.health}, Stamina={warrior.stamina}, Skills={warrior.skills}")
    print(f"Warrior 2: Health={warrior2.health}, Stamina={warrior2.stamina}, Skills={warrior2.skills}")

if __name__ == "__main__":
    main()
