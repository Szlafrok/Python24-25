import requests
from bs4 import BeautifulSoup
from pprint import pprint

def get_pokemon_info(id: int):
    url = f'https://pokeapi.co/api/v2/pokemon/{id}/'
    response = requests.get(url)
    return response.json()

def process_pokemon_info(id):
    pokemon = get_pokemon_info(id)
    pok_name = pokemon['name']
    pok_weight = pokemon['weight']
    pok_height = pokemon['height']
    pok_ability = pokemon['abilities'][0]['ability']['name']
    pok_type = pokemon['types'][0]['type']['name']

    return pok_name, pok_weight, pok_height, pok_ability, pok_type

def create_pokemon_dict(pok_id, pok_name, pok_weight, pok_height, pok_ability, pok_type, poks_dict):
    poks_dict[f"pok_{pok_id}"] = {
        "id": pok_id,
        "name": pok_name,
        "weight": pok_weight,
        "height": pok_height,
        "ability": pok_ability,
        "type": pok_type
    }

poks_dict = {}
ids = [25, 6, 94, 11, 54]
def main():
    try:
        for id in ids:
            pok_name, pok_weight, pok_height, pok_ability, pok_type = process_pokemon_info(id)
            create_pokemon_dict(id, pok_name, pok_weight, pok_height, pok_ability, pok_type, poks_dict)
    except:
        print(f"Nieprawidłowe id: {id}, nie ma takiego pokemona")

    pprint(poks_dict)

if __name__ == '__main__':
    main()

# Wymagania bazowe: 5 / 5
# Podział na słowniki: +2 / 2
# Czytelność kodu i type hinting: +2 / 3 - kod jest czytelny, można było dopisać parę komentarzy, ale to już drobnostka.

# 9p. Super!!