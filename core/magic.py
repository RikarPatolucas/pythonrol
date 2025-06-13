import random

class Spell:
    def __init__(self, name, cost, dmg, type, efecto=None):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        self.efecto = efecto

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)

    def tiene_efecto(self):
        return self.efecto is not None
