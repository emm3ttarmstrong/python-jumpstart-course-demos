

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print('{} attacks the {} (Level {})!'.format(self.name, creature.name, creature.level))

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return 'Creature: {} of level {}'.format(
            self.name, self.level
        )