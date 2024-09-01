from pokemon import getPokemon
from utils.cli_utils import parseInputs

if __name__ == '__main__':
    # import pprint
    
    # setup pretty printer for use
    # pp = pprint.PrettyPrinter(indent=4)
    
    # name = 'moltres'
    # nature = 'timid'
    # level = 100
    # evs = {'hp': 252, 'attack': 0, 'defense': 0, 'special-attack': 252, 'special-defense': 0, 'speed': 4}
    # ivs = {'hp': 31, 'attack': 31, 'defense': 31, 'special-attack': 31, 'special-defense': 31, 'speed': 31}
    name, nature, level, evs, ivs = parseInputs()

    # get a pokemon
    mon = getPokemon(name, nature, level, evs, ivs)

    # outputs
    # print(mon)
    # print(mon.types)
    # print(dir(mon))
    # print(mon.abilities[0].keys())
    # print(mon.abilities)
    # print(mon.valid_moves)