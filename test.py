from pokemon import Pokemon

def test_calculate_stats():
    evs = {'hp': 252, 'attack': 0, 'defense': 0, 'special-attack': 252, 'special-defense': 0, 'speed': 4}
    ivs = {'hp': 31, 'attack': 31, 'defense': 31, 'special-attack': 31, 'special-defense': 31, 'speed': 31}
    p = Pokemon("moltres", "timid", 100, evs, ivs)
    assert p.stats == {
        'hp': 384,
        'attack': 212,
        'defense': 216,
        'special-attack': 349,
        'special-defense': 206,
        'speed': 238
    }

def test_pokemon():
    evs = {'hp': 252, 'attack': 0, 'defense': 0, 'special-attack': 252, 'special-defense': 0, 'speed': 4}
    ivs = {'hp': 31, 'attack': 31, 'defense': 31, 'special-attack': 31, 'special-defense': 31, 'speed': 31}
    p = Pokemon("moltres", "timid", 100, evs, ivs)
    assert p.name == "moltres"
    assert p.nature == "timid"
    assert p.level == 100
    assert p.base_stats == {
        'hp': 90,
        'attack': 100,
        'defense': 90,
        'special-attack': 125,
        'special-defense': 85,
        'speed': 90
    }
    assert p.stats == {
        'hp': 384,
        'attack': 212,
        'defense': 216,
        'special-attack': 349,
        'special-defense': 206,
        'speed': 238
    }
    assert p.evs == evs
    assert p.ivs == ivs
    assert p.types == [
        {
            'name': 'fire',
            'damage_class': 'special',
            'damage_relations': {
                'double_damage_from': ['ground', 'rock', 'water'],
                'double_damage_to': ['bug', 'steel', 'grass', 'ice'],
                'half_damage_from': ['bug', 'steel', 'fire', 'grass', 'ice', 'fairy'],
                'half_damage_to': ['rock', 'fire', 'water', 'dragon'],
                'no_damage_from': [],
                'no_damage_to': []
            }
        }, {
            'name': 'flying',
            'damage_class': 'physical',
            'damage_relations': {
                'double_damage_from': ['rock', 'electric', 'ice'],
                'double_damage_to': ['fighting', 'bug', 'grass'],
                'half_damage_from': ['fighting', 'bug', 'grass'],
                'half_damage_to': ['rock', 'steel', 'electric'],
                'no_damage_from': ['ground'], 'no_damage_to': []
            }
        }
    ]
    assert p.abilities == [
        {
            'name': 'pressure',
            'is_hidden': False,
            'effect': "Moves targetting this Pokémon use one extra PP.\n\nThis ability stacks if multiple targets have it.  This ability still affects moves that fail or miss.  This ability does not affect ally moves that target either the entire field or just its side, nor this Pokémon's self-targetted moves; it does, however, affect single-targetted ally moves aimed at this Pokémon, ally moves that target all other Pokémon, and opponents' moves that target the entire field.  If this ability raises a move's PP cost above its remaining PP, it will use all remaining PP.\n\nWhen this Pokémon enters battle, all participating trainers are notified that it has this ability.\n\nOverworld: If the lead Pokémon has this ability, higher-levelled Pokémon have their encounter rate increased.",
            'short_effect': 'Increases the PP cost of moves targetting the Pokémon by one.',
            'flavor_text': 'Puts other Pokémon under pressure, causing them to expend more PP to use their moves.'
        },
        {
            'name': 'flame-body',
            'is_hidden': True,
            'effect': "Whenever a move makes contact with this Pokémon, the move's user has a 30% chance of being burned.\n\nOverworld: If any Pokémon in the party has this ability, each egg in the party has its hatch counter decreased by 2 (rather than 1) each step cycle, making eggs hatch roughly twice as quickly.  This effect does not stack if multiple Pokémon have this ability or magma armor.",
            'short_effect': 'Has a 30% chance of burning attacking Pokémon on contact.',
            'flavor_text': 'Contact with the Pokémon may burn the attacker.'
        }
    ]
    assert p.sprites == {
        'normal': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/146.png',
        'shiny': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/146.png'
    }
    assert p.valid_moves == [
        {'name': 'gust', 'level_learned_at': 1, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 40, 'pp': 35, 'priority': 0, 'type': 'flying'},
        {'name': 'wing-attack', 'level_learned_at': 15, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 60, 'pp': 35, 'priority': 0, 'type': 'flying'},
        {'name': 'fly', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 95, 'damage_class': 'physical', 'power': 90, 'pp': 15, 'priority': 0, 'type': 'flying'}, 
        {'name': 'take-down', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 85, 'damage_class': 'physical', 'power': 90, 'pp': 20, 'priority': 0, 'type': 'normal'},
        {'name': 'double-edge', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 120, 'pp': 15, 'priority': 0, 'type': 'normal'},
        {'name': 'leer', 'level_learned_at': 1, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'status', 'power': None, 'pp': 30, 'priority': 0, 'type': 'normal'}, 
        {'name': 'roar', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 20, 'priority': -6, 'type': 'normal'},
        {'name': 'ember', 'level_learned_at': 5, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 40, 'pp': 25, 'priority': 0, 'type': 'fire'}, 
        {'name': 'flamethrower', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 90, 'pp': 15, 'priority': 0, 'type': 'fire'},
        {'name': 'hyper-beam', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'special', 'power': 150, 'pp': 5, 'priority': 0, 'type': 'normal'},
        {'name': 'solar-beam', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 120, 'pp': 10, 'priority': 0, 'type': 'grass'},
        {'name': 'fire-spin', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 85, 'damage_class': 'special', 'power': 35, 'pp': 15, 'priority': 0, 'type': 'fire'},
        {'name': 'agility', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 30, 'priority': 0, 'type': 'psychic'},
        {'name': 'agility', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 30, 'priority': 0, 'type': 'psychic'},
        {'name': 'fire-blast', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 85, 'damage_class': 'special', 'power': 110, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'swift', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'special', 'power': 60, 'pp': 20, 'priority': 0, 'type': 'normal'},
        {'name': 'sky-attack', 'level_learned_at': 70, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'physical', 'power': 140, 'pp': 5, 'priority': 0, 'type': 'flying'},
        {'name': 'rest', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 5, 'priority': 0, 'type': 'psychic'},
        {'name': 'substitute', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 0, 'type': 'normal'},
        {'name': 'protect', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 4, 'type': 'normal'},
        {'name': 'sandstorm', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 0, 'type': 'rock'},
        {'name': 'endure', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 4, 'type': 'normal'},
        {'name': 'endure', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 4, 'type': 'normal'},
        {'name': 'sleep-talk', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 10, 'priority': 0, 'type': 'normal'},
        {'name': 'safeguard', 'level_learned_at': 10, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 25, 'priority': 0, 'type': 'normal'},
        {'name': 'rain-dance', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 5, 'priority': 0, 'type': 'water'},
        {'name': 'sunny-day', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'sunny-day', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'ancient-power', 'level_learned_at': 25, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 60, 'pp': 5, 'priority': 0, 'type': 'rock'},
        {'name': 'heat-wave', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'special', 'power': 95, 'pp': 10, 'priority': 0, 'type': 'fire'},
        {'name': 'heat-wave', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'special', 'power': 95, 'pp': 10, 'priority': 0, 'type': 'fire'},
        {'name': 'will-o-wisp', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 85, 'damage_class': 'status', 'power': None, 'pp': 15, 'priority': 0, 'type': 'fire'},
        {'name': 'facade', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 70, 'pp': 20, 'priority': 0, 'type': 'normal'},
        {'name': 'helping-hand', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 20, 'priority': 5, 'type': 'normal'},
        {'name': 'weather-ball', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 50, 'pp': 10, 'priority': 0, 'type': 'normal'},
        {'name': 'air-cutter', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 95, 'damage_class': 'special', 'power': 60, 'pp': 25, 'priority': 0, 'type': 'flying'},
        {'name': 'overheat', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'special', 'power': 130, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'overheat', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'special', 'power': 130, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'aerial-ace', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'physical', 'power': 60, 'pp': 20, 'priority': 0, 'type': 'flying'},
        {'name': 'roost', 'level_learned_at': 40, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 5, 'priority': 0, 'type': 'flying'},
        {'name': 'tailwind', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': None, 'damage_class': 'status', 'power': None, 'pp': 15, 'priority': 0, 'type': 'flying'},
        {'name': 'u-turn', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 70, 'pp': 20, 'priority': 0, 'type': 'bug'},
        {'name': 'flare-blitz', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 120, 'pp': 15, 'priority': 0, 'type': 'fire'},
        {'name': 'air-slash', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 95, 'damage_class': 'special', 'power': 75, 'pp': 15, 'priority': 0, 'type': 'flying'},
        {'name': 'air-slash', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 95, 'damage_class': 'special', 'power': 75, 'pp': 15, 'priority': 0, 'type': 'flying'},
        {'name': 'brave-bird', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 120, 'pp': 15, 'priority': 0, 'type': 'flying'},
        {'name': 'giga-impact', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'physical', 'power': 150, 'pp': 5, 'priority': 0, 'type': 'normal'},
        {'name': 'flame-charge', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 50, 'pp': 20, 'priority': 0, 'type': 'fire'},
        {'name': 'incinerate', 'level_learned_at': 30, 'learn_method': 'level-up', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 60, 'pp': 15, 'priority': 0, 'type': 'fire'},
        {'name': 'acrobatics', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 55, 'pp': 15, 'priority': 0, 'type': 'flying'},
        {'name': 'hurricane', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 70, 'damage_class': 'special', 'power': 110, 'pp': 10, 'priority': 0, 'type': 'flying'},
        {'name': 'hurricane', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 70, 'damage_class': 'special', 'power': 110, 'pp': 10, 'priority': 0, 'type': 'flying'},
        {'name': 'burning-jealousy', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 70, 'pp': 5, 'priority': 0, 'type': 'fire'},
        {'name': 'dual-wingbeat', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 90, 'damage_class': 'physical', 'power': 40, 'pp': 10, 'priority': 0, 'type': 'flying'},
        {'name': 'scorching-sands', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 70, 'pp': 10, 'priority': 0, 'type': 'ground'},
        {'name': 'tera-blast', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'special', 'power': 80, 'pp': 10, 'priority': 0, 'type': 'normal'},
        {'name': 'temper-flare', 'level_learned_at': 0, 'learn_method': 'machine', 'version': 'scarlet-violet', 'accuracy': 100, 'damage_class': 'physical', 'power': 75, 'pp': 10, 'priority': 0, 'type': 'fire'}
    ]

if __name__ == "__main__":
    test_pokemon()
    test_calculate_stats()
    print("All tests passed!")