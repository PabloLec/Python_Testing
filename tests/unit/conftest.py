import json
import pytest

from app import database as _DATABASE


@pytest.fixture(scope="session")
def SAMPLE_CLUBS(tmp_path_factory):
    clubs = {
        "clubs": [
            {"name": "Club Test 1", "email": "test1@test.com", "points": "20"},
            {"name": "Club Test 2", "email": "test2@test.com", "points": "10"},
            {"name": "Club Test 3", "email": "test3@test.com", "points": "1"},
        ]
    }

    clubs_file_path = tmp_path_factory.getbasetemp() / "clubs.json"

    with open(clubs_file_path, "w") as file:
        json.dump(clubs, file, indent=4)

    return clubs_file_path, clubs


@pytest.fixture(scope="session")
def SAMPLE_COMPETITIONS(tmp_path_factory):
    competitions = {
        "competitions": [
            {
                "name": "Competition Test 1",
                "date": "2100-03-27 10:00:00",
                "numberOfPlaces": 21,
            },
            {
                "name": "Competition Test 2",
                "date": "2100-03-27 10:00:00",
                "numberOfPlaces": 5,
            },
            {
                "name": "Competition Test 3",
                "date": "2000-03-27 10:00:00",
                "numberOfPlaces": 21,
            },
        ]
    }

    competitions_file_path = tmp_path_factory.getbasetemp() / "competitions.json"

    with open(competitions_file_path, "w") as file:
        json.dump(competitions, file, indent=4)

    return competitions_file_path, competitions


@pytest.fixture(scope="session")
def SAMPLE_DATABASE(SAMPLE_CLUBS, SAMPLE_COMPETITIONS):
    _DATABASE._DB_CLUBS_PATH = SAMPLE_CLUBS[0]
    _DATABASE._DB_COMPETITIONS_PATH = SAMPLE_COMPETITIONS[0]

    _DATABASE.load()

    return _DATABASE
