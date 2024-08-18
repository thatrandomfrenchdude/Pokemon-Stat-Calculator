import math
from pokemon import Pokemon

# reference
# https://bulbapedia.bulbagarden.net/wiki/Stat
# https://bulbapedia.bulbagarden.net/wiki/Damage

STAT_NAMES = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']

def calc_hp(
    base: int,
    iv: int,
    ev: int,
    level: int
) -> int:
    """
    Calculate the HP stat of a Pokemon Gen III or later.

    Args:
        base (int): The base HP stat of the Pokemon
        iv (int): The HP IV of the Pokemon
        ev (int): The HP EV of the Pokemon
        level (int): The level of the Pokemon

    Returns:
        int: The HP stat of the Pokemon
    """
    return math.floor((2 * base + iv + math.floor(ev / 4)) * level/100) + level + 10

def calc_stat(
    base: int,
    iv: int,
    ev: int,
    level: int
) -> int:
    """
    Calculate non-hp stats of a Pokemon Gen III or later.

    Args:
        base (int): The base stat of the Pokemon
        iv (int): The IV of the Pokemon
        ev (int): The EV of the Pokemon
        level (int): The level of the Pokemon

    Returns:
        int: The stat of the Pokemon
    """
    return math.floor(((2 * base + iv + math.floor(ev/4)) * level)/100) + 5

def calculate_stats(
    pokemon: Pokemon,
    evs: dict,
    ivs: dict
) -> dict:
    """
    Calculate the stats of a Pokemon.

    Args:
        pokemon (Pokemon): The Pokemon object
        evs (dict): The EVs of the Pokemon
        ivs (dict): The IVs of the Pokemon

    Returns:
        dict: The stats of the Pokemon
    """
    stats = {}

    # calculate the final stats
    for stat in STAT_NAMES:
        if stat == "hp":
            stats['hp'] = 1 if pokemon.name == "shedinja" else calc_hp(pokemon.base_stats['hp'], ivs['hp'], evs['hp'], pokemon.level)
        else:
            stats[stat] = calc_stat(pokemon.base_stats[stat], ivs[stat], evs[stat], pokemon.level)
    
    # handle nature
    for x in pokemon.nature_buffs:
        if pokemon.nature_buffs[x] == "null":
            break
        if x == "increased_stat":
            stats[pokemon.nature_buffs[x]] = int(stats[pokemon.nature_buffs[x]] * 1.1)
        if x == "decreased_stat":
            stats[pokemon.nature_buffs[x]] = int(stats[pokemon.nature_buffs[x]] * 0.9)
    
    return stats

def calculate_damage():
    pass
