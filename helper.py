import json
from datetime import datetime


def load_clubs():
    with open("clubs.json") as file:
        return json.load(file)["clubs"]


def load_competitions():
    with open("competitions.json") as file:
        return json.load(file)["competitions"]


def get_club_by_mail(mail: str):
    selected_club = None
    for club in CLUBS:
        if club["email"] == mail:
            selected_club = club
            break

    return selected_club


def get_club_by_name(name: str):
    selected_club = None
    for club in CLUBS:
        if club["name"] == name:
            selected_club = club
            break

    return selected_club


def get_competition_by_name(name: str):
    selected_competition = None
    for competition in COMPETITIONS:
        if competition["name"] == name:
            selected_competition = competition
            break

    return selected_competition


def get_max_places(club: dict):
    return min(int(club["points"]), 12)


def is_competition_date_correct(date: str):
    date_time_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return datetime.today() > date_time_obj


def is_purchase_valid(competition: str, club: str, places: str):
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(club=club):
        return False

    return True


COMPETITIONS = load_competitions()
CLUBS = load_clubs()
USER_CLUB = None
