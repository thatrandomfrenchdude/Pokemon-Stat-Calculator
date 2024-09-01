import requests

pokemon_base_url = "http://pokeapi.co/api/v2/pokemon/"
nature_base_url = "http://pokeapi.co/api/v2/nature/"

def processAbilities(a):
    def handleAbilityInfo(url):
        try:
            ability_info = requests.get(url).json()

            effect = None
            short_effect = None
            for ee in ability_info['effect_entries']:
                if ee['language']['name'] == 'en':
                    effect = ee['effect']
                    short_effect = ee['short_effect']
                    break
            
            flavor_text = None
            for fte in ability_info['flavor_text_entries']:
                if fte['language']['name'] == 'en' and fte['version_group']['name'] == 'scarlet-violet':
                    flavor_text = fte['flavor_text']
                    break

            return effect, short_effect, flavor_text

        except Exception as e:
            print(f"Error fetching ability info: {e}")
            ability_info = {}
        return ability_info
    abilities = []

    for ability in a:
        # use the url to get the ability info
        url = ability['ability']['url']
        effect, short_effect, flavor_text = handleAbilityInfo(url)

        abilities.append(
            {
                "name": ability['ability']['name'],
                "is_hidden": ability['is_hidden'],
                "effect": effect,
                "short_effect": short_effect,
                "flavor_text": flavor_text
            }
        )

    return abilities

def processMoves(moves):
    try:
        scarlet_violet_moves = []
        for m in moves:
            move = {
                "move": {},
                "version_group_details": {}
            }
            for version in m['version_group_details']:
                if version['version_group']['name'] == 'scarlet-violet':
                    move["move"] = m['move']
                    move["version_group_details"] = version
                    scarlet_violet_moves.append(move)
        return scarlet_violet_moves
    except Exception as e:
        print(f"Error processing moves: {e}")
        return []

def processTypes(types):
    def handleTypeInfo(url):
        try:
            type_info = requests.get(url).json()

            damage_class = type_info['move_damage_class']['name']
            # damage_relations = type_info['damage_relations']
            damage_relations = {}

            for key, value in type_info['damage_relations'].items():
                damage_relations[key] = [x['name'] for x in value]
        except Exception as e:
            print(f"Error fetching type info: {e}")
            damage_class = "null"
            damage_relations = {}

        return damage_class, damage_relations

    try:
        typing = []

        # handle the types
        for type in types:
            # use the url to get the type info
            url = type['type']['url']
            damage_class, damage_relations = handleTypeInfo(url)

            typing.append(
                {
                    "name": type['type']['name'],
                    "damage_class": damage_class,
                    "damage_relations": damage_relations
                }
            )

        return typing
    except Exception as e:
        print(f"Error processing types: {e}")
        return []

def processSprites(sprites):
    return {
        "normal": sprites['front_default'],
        "shiny": sprites['front_shiny']
    }