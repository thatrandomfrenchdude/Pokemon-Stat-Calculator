from pokemon import Pokemon
from calculations import calculate_stats

def test_pokemon():
    p = Pokemon("moltres", "timid", 100)
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
    assert p.nature_buffs == {
        'increased_stat': 'speed',
        'decreased_stat': 'attack'
    }

def test_calculate_stats():
    p = Pokemon("moltres", "timid", 100)
    evs = {'hp': 252, 'attack': 0, 'defense': 0, 'special-attack': 252, 'special-defense': 0, 'speed': 4}
    ivs = {'hp': 31, 'attack': 31, 'defense': 31, 'special-attack': 31, 'special-defense': 31, 'speed': 31}
    stats = calculate_stats(p, evs, ivs)
    assert stats == {
        'hp': 384,
        'attack': 212,
        'defense': 216,
        'special-attack': 349,
        'special-defense': 206,
        'speed': 238
    }

if __name__ == "__main__":
    test_pokemon()
    test_calculate_stats()
    print("All tests passed!")