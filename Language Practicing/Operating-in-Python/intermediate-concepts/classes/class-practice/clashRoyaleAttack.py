# Practicing Object-oriented programming, but object-to-object interaction

# Below is object-to-object interaction, a core part of object-oriented programming (OOP)
class ClashRoyale:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    # Reminder: self = the current object doing the action (miniPekka)
    # opponent = a completely separate object of the same class, passed in as an argument
    def attack(self, opponent):
        attacked = opponent.hp - self.damage
        if (attacked <= 0):
            print(f"{self.name} destroyed the {opponent.name}")
        else:
            print(f"{opponent.name} is still alive! More damage to do")

# miniPekka is a whole object — an instance of the class ClashRoyale
miniPekka = ClashRoyale("mini p.e.k.k.a", 300, 150)
# electroWizard is a whole object — an instance of the class ClashRoyale
electroWizard = ClashRoyale("electro wizard", 100, 20)

# In OOP: methods can take other objects as input to interact with their properties
miniPekka.attack(electroWizard)

