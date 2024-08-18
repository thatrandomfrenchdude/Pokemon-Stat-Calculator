import argparse
from sys import argv

import calculations
import pokemon

def main():
    evs = {}
    ivs = {}

    # get the pokemon info via command line or input
    if len(argv) == 2:
        # get the pokemon's name, nature, and level
        name = input('Enter Pokémon\'s name: ').lower()
        nature = input('Enter Pokémon\'s nature: ').lower()
        level = int(input('Enter Pokémon\'s level: '))

        print('Enter the following stats in order:\nHP, Attack, Defense, Special Attack, Special Defense, and Speed')

        # get the variable stats
        for pair in zip(
            calculations.STAT_NAMES,
            list(map(int, input('Enter the Pokémon\'s EVs (space separated.): ').split())),
            list(map(int, input('Enter the Pokémon\'s IVs (space separated.): ').split()))
        ):
            evs[pair[0]] = pair[1]
            ivs[pair[0]] = pair[2]
    else:
        parser = argparse.ArgumentParser(description="Handle Pokemon from commandline")
        parser.add_argument('name', metavar="[name]", type=str)
        parser.add_argument('-ev', '--EVs', metavar='EV', type=int, nargs=6)
        parser.add_argument('-iv', '--IVs', metavar='IV', type=int, nargs=6)
        parser.add_argument('-n', '--nature', metavar='nature', type=str, nargs=1)
        parser.add_argument('-l', '--level', metavar='level', type=int, nargs=1)

        #parses all of the arguments into  a list of their respective types and stores them in args
        args = parser.parse_args()

        # get the pokemon's name, nature, and level
        name = str(args.name).lower()
        nature = ''.join(args.nature)
        level = args.level[0]

        # get the variable stats
        for pair in zip(
            calculations.STAT_NAMES,
            args.EVs,
            args.IVs
        ):
            evs[pair[0]] = pair[1]
            ivs[pair[0]] = pair[2]

    # make the pokemon
    try:
        mon = pokemon.Pokemon(name, nature, level)
    except ValueError as e:
        print(e)
        exit()

    # calculate the final stats
    stats = calculations.calculate_stats(mon, evs, ivs)

    print(mon)
    for stat in stats:
        print(f"{stat.capitalize()}: {stats[stat]}")

if __name__ == '__main__':
    main()