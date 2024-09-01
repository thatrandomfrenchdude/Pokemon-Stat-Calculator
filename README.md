# Pokemon-Stat-Calculator
A python Pokemon stat calculator using https://pokeapi.co/

## Setup
Install requirements with:
```
pip install -r requirements.txt
```

## Usage
### Specific pokemon and values
Arguments:
* `-n`, `--nature` - sets the nature
* `-ev`, `--EVs` - sets the EVs, ordered by HP, Atk, Def, SpA, SpD, Spe
* `-iv`, `--IVs` - sets the IVs, ordered by HP, Atk, Def, SpA, SpD, Spe
* `-l`, `--level [level]` - sets the level
```
# general usage:
python main.py [name] -n [nature] -ev [hp] [attack] [defense] [special attack] [special defense] [speed] -iv [hp] [attack] [defense] [special attack] [special defense] [speed] -l [level]

# specific example:
python main.py moltres -n timid -ev 252 0 0 252 0 4 -iv 31 31 31 31 31 31 -l 100
```

### Walkthrough
Asks for each item one at a time.
```
python main.py
```

## Testing
Run using pytest:
```
pytest test.py
```

## Notes
Please be aware that not all pokemon are working yet as I continue to build this.<br>
For example, regional variants are not supported and I have not added error catching for all cases.