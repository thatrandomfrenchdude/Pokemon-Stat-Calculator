import requests

class Pokemon():
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
    """
    pokemon_base_url = "http://pokeapi.co/api/v2/pokemon/"
    nature_base_url = "http://pokeapi.co/api/v2/nature/"
    base_stats = {}
    name = ""
    nature = ""
    nature_buffs = {}
    level: int

    def __init__(self, name, nature, level):
        self.level = level

        # get the pokemon info
        res = requests.get(self.pokemon_base_url + name).json()
        if res == {"detail":"Not found."}:
            raise ValueError("Invalid Pokemon name. Exiting...")
        else:
            self.name = name
            self.base_stats = {x['stat']['name']: x['base_stat'] for x in res['stats']}

        # get the nature info
        r = requests.get(self.nature_base_url + nature).json()
        if r == {"detail":"Not found."}:
            raise ValueError("Invalid nature. Exiting...")
        else:
            self.nature = nature
            try:
                self.nature_buffs['increased_stat'] = r['increased_stat']['name']
                self.nature_buffs['decreased_stat'] = r['decreased_stat']['name']
            except TypeError:
                self.nature_buffs['increased_stat'] = 'null'
                self.nature_buffs['decreased_stat'] = 'null'

    def __str__(self) -> str:
        return f"\n{self.name.capitalize()}\nLv {self.level}\n{self.nature.capitalize()} nature"