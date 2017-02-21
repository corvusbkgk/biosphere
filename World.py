class Location:
    def __init__(self):
        self.animals = []
        self.plants = []
        # TODO: remove debug food
        self.debugFood = 1000000
        self.dfPerTick = 1000

class World:
    def __init__(self):
        self.locations = []

    def tick(self):
        for loc in self.locations:
            for pop in loc.animals:
                # Stage 1: build hunger
                pop.hunger = pop.hunger - pop.species.metabolism
                # Stage 2: Choose targets
                if pop.species.isCarnivore:
                    pop.targets = []
                    for victim in loc.animals:
                        if victim.species.canBeEaten(pop):
                            pop.targets.append(victim)
                else:
                    loc.debugFood -= pop.species.metabolism * pop.count
            # All targets are set at this point
            for pop in loc.animals:
                # Stage 3: TODO Eat
                pass
                # Stage 4: TODO Die of hunger
            loc.debugFood = loc.debugFood + loc.dfPerTick
