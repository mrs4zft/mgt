import pandas as pd
from pandas import DataFrame
import requests
import sys

URL = "https://archidekt.com/api/decks/"

def fetch_deck(id):
    deck_url = URL+id+'/'
    print(deck_url)
    response = requests.get(deck_url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return pd.DataFrame()


def get_decklist(data):
    deck_list = []
    cards = data['cards']
    for card in cards:
        c = card['card']
        oc = c['oracleCard']
        deck_list.append(oc['name'])

    return deck_list


def get_simple_decklist(path):
    deck_list = pd.read_csv(path)
    return deck_list


def match_card(card_names, name):
    if (card_names == name).any():
        return 1
    else: 
        return 0


def main():
    id = sys.argv[1]
    method = sys.argv[2]
    print(id)
    collection = pd.read_csv("./data/Inventory_Ameisenstaat_2025.April.12.csv")
    card_names = collection.Name
    if method == "arch":
        deck_data = fetch_deck(id)
    else:
        deck_data = get_simple_decklist(id)

    match = 0
    if (type(deck_data) == DataFrame and deck_data.empty):
        return
    else:
        if method == "arch":
            deck_list = get_decklist(deck_data)
        else:
            deck_list = deck_data["name"]
        for name in deck_list:
            match = match + match_card(card_names, name)
            print(name)
    print(match)


if __name__ == "__main__":
    main()
    


