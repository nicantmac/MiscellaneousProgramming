class ClashRoyale:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, opponent):
        attacked = opponent.hp - self.damage
        if (attacked <= 0):
            print(f"{self.name} destroyed the {opponent.name}")
        else:
            print(f"{opponent.name} is still alive! More damage to do")

miniPekka = ClashRoyale("mini p.e.k.k.a", 300, 150)
RoyalGuard = ClashRoyale("electro wizard", 100, 20)

miniPekka.attack(RoyalGuard)
