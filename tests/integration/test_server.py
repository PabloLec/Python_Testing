def test_index(CLIENT):
    response = CLIENT.get("/")

    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_login(CLIENT, SAMPLE_DATABASE):
    response_invalid  = CLIENT.post('/showSummary', data=dict(
            email="foo@bar.com",
        ), follow_redirects=True)

    assert response_invalid.status_code == 200
    assert b'Email address not found' in response_invalid.data

    response = CLIENT.post('/showSummary', data=dict(
                email="test1@test.com",
            ), follow_redirects=True)
    
    assert response.status_code == 200
    assert b'test1@test.com' in response.data

def test_competition_listing(CLIENT):
    response = CLIENT.post('/showSummary', data=dict(
                    email="test1@test.com",
                ), follow_redirects=True)

    assert b'Competition Test 1' in response.data
    assert b'Competition Test 2' in response.data
    assert b'Competition Test 3' not in response.data
    
def test_booking_display(CLIENT):
    response = CLIENT.get("/book/Competition Test 1/Club Test 1")

    assert response.status_code == 200
    assert b'Competition Test 1' in response.data
    assert b'Places available: 21' in response.data
    assert b'max="12"' in response.data

def test_purchase(CLIENT, SAMPLE_DATABASE):
    initial_places = int(SAMPLE_DATABASE.COMPETITIONS[0]["numberOfPlaces"])
    initial_points = int(SAMPLE_DATABASE.CLUBS[0]["points"])

    response = CLIENT.post('/purchasePlaces', data=dict(
                    competition="Competition Test 1",
                    club="Club Test 1",
                    places=5
                ), follow_redirects=True)

    assert response.status_code == 200
    assert b'Great-booking complete!' in response.data
    assert int(SAMPLE_DATABASE.COMPETITIONS[0]["numberOfPlaces"]) == initial_places - 5
    assert int(SAMPLE_DATABASE.CLUBS[0]["points"]) == initial_points - 5

    response_invalid = CLIENT.post('/purchasePlaces', data=dict(
                        competition="Competition Test 1",
                        club="Club Test 1",
                        places=15
                    ), follow_redirects=True)

    assert b'Something went wrong' in response_invalid.data

def test_club_list(CLIENT, SAMPLE_DATABASE):
    response = CLIENT.get("/clubs")

    assert response.status_code == 200

    for club in SAMPLE_DATABASE.CLUBS:
        assert club["name"] in str(response.data)

def test_logout(CLIENT):
    response = CLIENT.get("/logout", follow_redirects=True)

    assert b'Welcome to the GUDLFT' in response.data
