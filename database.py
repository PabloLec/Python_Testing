import json


def load_clubs():
    with open("clubs.json") as file:
        return json.load(file)["clubs"]


def load_competitions():
    with open("competitions.json") as file:
        return json.load(file)["competitions"]


def register_purchase(competition: str, club: str, places: str):
    for i in range(len(COMPETITIONS)):
        if COMPETITIONS[i]["name"] == competition["name"]:
            COMPETITIONS[i]["numberOfPlaces"] = int(COMPETITIONS[i]["numberOfPlaces"]) - int(places)

    for i in range(len(CLUBS)):
        if CLUBS[i]["name"] == club["name"]:
            CLUBS[i]["points"] = int(CLUBS[i]["points"]) - int(places)

    _save_competitions()
    _save_clubs()


def _save_clubs():
    with open("clubs.json", "w") as file:
        return json.dump({"clubs": CLUBS}, file, indent=4)


def _save_competitions():
    with open("competitions.json", "w") as file:
        return json.dump({"competitions": COMPETITIONS}, file, indent=4)


COMPETITIONS = load_competitions()
CLUBS = load_clubs()
