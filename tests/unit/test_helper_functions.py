from app import helper as _HELPER


def test_get_club_by_mail(SAMPLE_DATABASE):
    club1 = _HELPER.get_club_by_mail(mail="test1@test.com")
    club2 = _HELPER.get_club_by_mail(mail="test2@test.com")
    club_none = _HELPER.get_club_by_mail(mail="foo")

    assert club1 == SAMPLE_DATABASE.CLUBS[0]
    assert club2 == SAMPLE_DATABASE.CLUBS[1]
    assert club_none is None


def test_get_club_by_name(SAMPLE_DATABASE):
    club1 = _HELPER.get_club_by_name(name="Club Test 1")
    club2 = _HELPER.get_club_by_name(name="Club Test 2")
    club_none = _HELPER.get_club_by_name(name="foo")

    assert club1 == SAMPLE_DATABASE.CLUBS[0]
    assert club2 == SAMPLE_DATABASE.CLUBS[1]
    assert club_none is None


def test_get_competition_by_name(SAMPLE_DATABASE):
    competition1 = _HELPER.get_competition_by_name(name="Competition Test 1")
    competition2 = _HELPER.get_competition_by_name(name="Competition Test 2")
    competition_none = _HELPER.get_competition_by_name(name="foo")

    assert competition1 == SAMPLE_DATABASE.COMPETITIONS[0]
    assert competition2 == SAMPLE_DATABASE.COMPETITIONS[1]
    assert competition_none is None


def test_get_max_places(SAMPLE_DATABASE):
    places_10 = _HELPER.get_max_places(
        competition=SAMPLE_DATABASE.COMPETITIONS[0], club=SAMPLE_DATABASE.CLUBS[0]
    )
    places_5 = _HELPER.get_max_places(
        competition=SAMPLE_DATABASE.COMPETITIONS[1], club=SAMPLE_DATABASE.CLUBS[1]
    )
    places_1 = _HELPER.get_max_places(
        competition=SAMPLE_DATABASE.COMPETITIONS[0], club=SAMPLE_DATABASE.CLUBS[2]
    )

    assert places_10 == 10
    assert places_5 == 5
    assert places_1 == 1


def test_is_date_future():
    date1 = "2000-01-01 10:10:10"
    date2 = "2100-01-01 10:10:10"

    assert not _HELPER.is_date_future(date=date1)
    assert _HELPER.is_date_future(date=date2)


def test_get_future_competitions(SAMPLE_DATABASE):
    future_competitions = _HELPER.get_future_competitions(
        competitions=SAMPLE_DATABASE.COMPETITIONS
    )

    assert len(future_competitions) == 2
    assert future_competitions[0] == SAMPLE_DATABASE.COMPETITIONS[0]
    assert future_competitions[1] == SAMPLE_DATABASE.COMPETITIONS[1]


def test_is_purchase_valid(SAMPLE_DATABASE):
    purchase_pass = _HELPER.is_purchase_valid(
        competition=SAMPLE_DATABASE.COMPETITIONS[0],
        club=SAMPLE_DATABASE.CLUBS[0],
        places="3",
    )
    purchase_too_much_places = _HELPER.is_purchase_valid(
        competition=SAMPLE_DATABASE.COMPETITIONS[0],
        club=SAMPLE_DATABASE.CLUBS[2],
        places="5",
    )

    assert purchase_pass
    assert not purchase_too_much_places

    purchase_var_not_set = _HELPER.is_purchase_valid(
        competition=None, club=SAMPLE_DATABASE.CLUBS[0], places="3"
    )
    purchase_places_not_numeric = _HELPER.is_purchase_valid(
        competition=SAMPLE_DATABASE.COMPETITIONS[0],
        club=SAMPLE_DATABASE.CLUBS[0],
        places="foo",
    )

    assert not purchase_var_not_set
    assert not purchase_places_not_numeric
