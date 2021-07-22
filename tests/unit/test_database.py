import pytest

def test_load_database(SAMPLE_DATABASE, SAMPLE_CLUBS, SAMPLE_COMPETITIONS):
    assert SAMPLE_DATABASE.CLUBS == SAMPLE_CLUBS[1]["clubs"]
    assert SAMPLE_DATABASE.COMPETITIONS == SAMPLE_COMPETITIONS[1]["competitions"]


def test_register_purchase(SAMPLE_DATABASE):
    SAMPLE_DATABASE.register_purchase(
        competition=SAMPLE_DATABASE.COMPETITIONS[0],
        club=SAMPLE_DATABASE.CLUBS[0],
        places="10",
    )

    assert SAMPLE_DATABASE.CLUBS[0]["points"] == 10
    assert SAMPLE_DATABASE.COMPETITIONS[0]["numberOfPlaces"] == 11

def test_register_purchase_invalid_competition(SAMPLE_DATABASE):
    unknown_competition = {"name": "foo"}

    with pytest.raises(ValueError):
        SAMPLE_DATABASE.register_purchase(
                competition=unknown_competition,
                club=SAMPLE_DATABASE.CLUBS[0],
                places="10",
        )

def test_register_purchase_invalid_club(SAMPLE_DATABASE):
    unknown_club= {"name": "foo"}

    with pytest.raises(ValueError):
        SAMPLE_DATABASE.register_purchase(
                competition=SAMPLE_DATABASE.COMPETITIONS[0],
                club=unknown_club,
                places="10",
        )

def test_save_database(SAMPLE_DATABASE):
    SAMPLE_DATABASE.load()

    assert SAMPLE_DATABASE.CLUBS[0]["points"] == 10
    assert SAMPLE_DATABASE.COMPETITIONS[0]["numberOfPlaces"] == 11
