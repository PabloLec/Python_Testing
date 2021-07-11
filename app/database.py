import json
from pathlib import Path

_DB_CLUBS_PATH = Path(__file__).resolve().parent / "db/clubs.json"
_DB_COMPETITIONS_PATH = Path(__file__).resolve().parent / "db/competitions.json"

def load_clubs():
    with open(_DB_CLUBS_PATH) as file:
        return json.load(file)["clubs"]


def load_competitions():
    with open(_DB_COMPETITIONS_PATH) as file:
        return json.load(file)["competitions"]


def register_purchase(competition: str, club: str, places: str):
    for i in range(len(COMPETITIONS)):
        if COMPETITIONS[i]["name"] == competition["name"]:
            COMPETITIONS[i]["numberOfPlaces"] = int(COMPETITIONS[i]["numberOfPlaces"]) - int(places)
            break
        elif i == len(COMPETITIONS) - 1:
            raise ValueError

    for i in range(len(CLUBS)):
        if CLUBS[i]["name"] == club["name"]:
            CLUBS[i]["points"] = int(CLUBS[i]["points"]) - int(places)
            break
        elif i == len(CLUBS) - 1:
            raise ValueError

    _save_competitions()
    _save_clubs()


def _save_clubs():
    with open(_DB_CLUBS_PATH, "w") as file:
        json.dump({"clubs": CLUBS}, file, indent=4)


def _save_competitions():
    with open(_DB_COMPETITIONS_PATH, "w") as file:
        json.dump({"competitions": COMPETITIONS}, file, indent=4)


def load():
    global COMPETITIONS
    global CLUBS

    COMPETITIONS = load_competitions()
    CLUBS = load_clubs()

CLUBS = None
COMPETITIONS = None
