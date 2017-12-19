import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon

def main():
    print_header()
    game_loop()

def print_header():
    print('----------------------------------------')
    print('             WIZARD GAME')
    print('----------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger',12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon',50, 100, True),
        Wizard('Evil Wizard', 1000)

    ]


    hero = Wizard('Gandalf', 75)

    round_count = 1


    while True:

        active_creature = random.choice(creatures)

        print()
        print('A {} of level {} has appeared!'.format(active_creature.name, active_creature.level))

        cmd = input("Do you want to (a)ttack, (r)un away, or (l)ook around? ").lower()

        if cmd =='a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard retreats to regain his strength!")
                time.sleep(5)
                print("The wizard returns, revitalized.")


        elif cmd == 'r':
            print('run away')

        elif cmd  == 'l':
            print('The wizard looks around the surrounding area and sees:')
            for c in creatures:
                print("A {}, level {}".format(c.name, c.level))

        else:
            print('Ok, exiting game. Goodbye.')
            break

        if not creatures:
            print("You've defeated all the creatures!")
            break

if __name__ == '__main__':
    main()