class Population:
    def __init__(self, species, count):
        self.species = species
        self.count   = count

class Species:
    def __init__(self):
        self.isCarnivore = False
        self.size = 5
        self.metabolism = 10
        pass

    def canBeEaten(self, predator):
        return self.size < predator.size

    def canEat(self, victim):
        return self.isCarnivore and victim.canBeEaten(self)