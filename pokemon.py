import requests

from utils.api_utils import *
from utils.stat_utils import *


class Pokemon:
    """
    This class fetches information about a Pokemon from the pokeapi.co API.

    Args:
        name (str): The name of the Pokemon.
        nature (str): The nature of the Pokemon.
        level (int): The level of the Pokemon.

    Attributes:
        pokemon_base_url (str): The base URL for the Pokemon API.
        nature_base_url (str): The base URL for the Nature API.
        stats (dict): The stats of the Pokemon.
        name (str): The name of the Pokemon.
        nature (dict): The nature of the Pokemon.
        hp (int): The HP of the Pokemon.
        level (int): The level of the Pokemon.
        stats (dict): The final stats of the Pokemon.
        evs (dict): The EVs of the Pokemon.
        ivs (dict): The IVs of the Pokemon.
        valid_moves (list): The valid moves of the Pokemon.
        types (list): The types of the Pokemon.
        abilities (list): The abilities of the Pokemon.
        sprites (dict): The sprites of the Pokemon.
    """
    name = ""
    nature = ""
    level: int
    base_stats = {}
    stats = {}
    evs = {}
    ivs = {}
    types = []
    abilities = [] # for scarlet and violet
    valid_moves = [] # for scarlet and violet
    sprites = {
        "normal": "",
        "shiny": ""
    }

    def __init__(
        self,
        name,
        nature,
        level,
        evs,
        ivs
    ):
        self.level = level
        self.evs = evs
        self.ivs = ivs

        # get the pokemon info
        res = requests.get(pokemon_base_url + name).json()
        if res == {"detail":"Not found."}:
            raise ValueError("Invalid Pokemon name. Exiting...")
        else:
            self.name = name
            self.base_stats = {x['stat']['name']: x['base_stat'] for x in res['stats']}
            self.sprites = processSprites(res['sprites'])
            self.valid_moves = processMoves(res['moves'])
            self.types = processTypes(res['types'])
            self.abilities = processAbilities(res['abilities'])

        # get the nature info
        r = requests.get(nature_base_url + nature).json()
        nature_buffs = {}
        if r == {"detail":"Not found."}:
            raise ValueError("Invalid nature. Exiting...")
        else:
            self.nature = nature
            try:
                nature_buffs['increased_stat'] = r['increased_stat']['name']
                nature_buffs['decreased_stat'] = r['decreased_stat']['name']
            except TypeError:
                nature_buffs['increased_stat'] = 'null'
                nature_buffs['decreased_stat'] = 'null'

        # calc stats
        self.stats = calculate_stats(
            self.name,
            self.level,
            self.base_stats,
            nature_buffs,
            self.evs,
            self.ivs
        )

    def __str__(self) -> str:
        outstring = f"Lv {self.level} {self.nature.capitalize()} {self.name.capitalize()}"
        for stat in self.stats:
            outstring += f"\n{stat.capitalize()}: {self.stats[stat]}"
        return outstring
    
def getPokemon(
    name: str,
    nature: str,
    level: int,
    evs: dict,
    ivs: dict
) -> Pokemon:
    """
    Create a pokemon object and calculate its stats

    Args:
        name (str): The name of the pokemon
        nature (str): The nature of the pokemon
        level (int): The level of the pokemon
        evs (dict): The EVs of the pokemon
        ivs (dict): The IVs of the pokemon
    """
    
    try:
        return Pokemon(name, nature, level, evs, ivs)
    except ValueError as e:
        print(e)
        exit()