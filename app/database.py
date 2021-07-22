import json
from pathlib import Path

_DB_CLUBS_PATH = Path(__file__).resolve().parent / "db/clubs.json"
_DB_COMPETITIONS_PATH = Path(__file__).resolve().parent / "db/competitions.json"


def load_clubs():
    """Load club from database.

    Returns:
        dict: DB clubs.
    """
    with open(_DB_CLUBS_PATH, 'r') as file:
        return json.load(file)["clubs"]


def load_competitions():
    """Load competition from database.

    Returns:
        dict: DB competitions.
    """
    with open(_DB_COMPETITIONS_PATH, 'r') as file:
        return json.load(file)["competitions"]


def register_purchase(competition: str, club: str, places: str):
    """Substract booked places from competition available places and
    club points count.

    Args:
        competition (str): Booked competition.
        club (str): User club.
        places (str): Number of booked places.

    Raises:
        ValueError: If competition or club is not found in DB.
    """
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
    """Save cached clubs in JSON DB."""
    with open(_DB_CLUBS_PATH, "w") as file:
        json.dump({"clubs": CLUBS}, file, indent=4)


def _save_competitions():
    """Save cached competitions in JSON DB."""
    with open(_DB_COMPETITIONS_PATH, "w") as file:
        json.dump({"competitions": COMPETITIONS}, file, indent=4)


def load():
    """Initiate club and competitions loading."""
    global COMPETITIONS
    global CLUBS

    COMPETITIONS = load_competitions()
    CLUBS = load_clubs()


CLUBS = None
COMPETITIONS = None
