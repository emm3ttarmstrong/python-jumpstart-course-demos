import random

from actors import Wizard, Creature

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
        Creature('Toad', 1),
        Creature('Tiger',12),
        Creature('Bat', 3),
        Creature('Dragon',50),
        Creature('Evil Wizard', 1000)

    ]


    hero = Wizard('Gandalf', 75)




    while True:

        active_creature = random.choice(creatures)
        print()
        print('A {} of level {} has appeared!'.format(active_creature.name, active_creature.level))

        cmd = input("Do you want to (a)ttack, (r)un away, or (l)ook around? ").lower()
        if cmd =='a':
            hero.attack(active_creature)


        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print('Ok, exiting game. Goodbye.')
            break


if __name__ == '__main__':
    main()