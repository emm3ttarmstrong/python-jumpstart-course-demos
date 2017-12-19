import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature: {} of level {}'.format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1,12) * self.level

class Wizard(Creature):
    def __init__(self, name, level):
        super().__init__(name, level)

    def attack(self, creature):
        print('{} attacks the {} (Level {})!'.format(self.name, creature.name, creature.level))

        my_roll = self.get_defensive_roll()
        #creature_roll = random.randint(1,12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("You roll {}.".format(my_roll))
        print("{} rolls {}.".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has defeated a {}!".format(creature.name))
            return True
        else:
            print("The wizard has been wounded by a {}.".format(creature.name))
            return False

class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return int(base_roll/2)

class Dragon(Creature):
    def __init__(self, name, level, scaliness, breathes_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        fire_modifier = 5 if self.breathes_fire else 1
        scale_modifier = self.scaliness/10
        return int(base_roll * fire_modifier * scale_modifier)
