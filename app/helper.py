from datetime import datetime

from app import database as _DATABASE


def get_club_by_mail(mail: str):
    """Get a club associated with given email address.

    Args:
        mail (str): Email address.

    Returns:
        dict: Club associated with given email address.
    """
    selected_club = None
    for club in _DATABASE.CLUBS:
        if club["email"] == mail:
            selected_club = club
            break

    return selected_club


def get_club_by_name(name: str):
    """Get a club based on its name.

    Args:
        name (str): Club name.

    Returns:
        dict: Found club dict.
    """
    selected_club = None
    for club in _DATABASE.CLUBS:
        if club["name"] == name:
            selected_club = club
            break

    return selected_club


def get_competition_by_name(name: str):
    """Get a competition based on its name.

    Args:
        name (str): Competition name.

    Returns:
        dict: Found competition dict.
    """
    selected_competition = None
    for competition in _DATABASE.COMPETITIONS:
        if competition["name"] == name:
            selected_competition = competition
            break

    return selected_competition


def get_max_places(competition: dict, club: dict):
    """Get maximum places bookable places for a given competition and a given club.
    NB: A club can only book 12 places max at once.

    Args:
        competition (dict): Competition to be considered.
        club (dict): Club to be considered.

    Returns:
        int: Maximum bookable places.
    """
    return min(int(club["points"]), int(competition["numberOfPlaces"]), 12)


def is_date_future(date: str):
    """Verify if a given date is later than today.

    Args:
        date (str): Date string to be considered.

    Returns:
        bool: Date is future.
    """
    date_time_obj = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

    return datetime.today() < date_time_obj


def get_future_competitions(competitions: list):
    """Get list of future competitions.

    Args:
        competitions (list): All competitions in DB.

    Returns:
        list: List of future competitions.
    """
    return [x for x in competitions if is_date_future(x["date"])]


def is_purchase_valid(competition: dict, club: dict, places: str):
    """Verify if a purchase request is valid.

    Args:
        competition (dict): Competition to be booked.
        club (dict): User's club.
        places (str): Number of places to be booked.

    Returns:
        bool: Purchase is valid.
    """
    if not competition or not club:
        return False
    if not places.isnumeric():
        return False
    if not 0 < int(places) <= get_max_places(competition=competition, club=club):
        return False

    return True
