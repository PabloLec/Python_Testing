from locust import HttpUser, task, between
from random import randint
from tests.locust import locust_helper as _HELPER


class User(HttpUser):
    wait_time = between(1, 2.5)

    @task(10)
    def get_index(self):
        self.client.get("/")

    @task(8)
    def login(self):
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        email_address = _DATABASE.CLUBS[club_num]["email"]
        self.client.post("/showSummary", {"email": email_address})

    @task(6)
    def booking_menu(self):
        competition_num = randint(0, len(_DATABASE.COMPETITIONS) - 1)
        competition = _DATABASE.COMPETITIONS[competition_num]["name"]
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        club = _DATABASE.CLUBS[club_num]["name"]
        self.client.get(f"/book/{competition}/{club}")

    @task(3)
    def purchase_places(self):
        competition_num = randint(0, len(_DATABASE.COMPETITIONS) - 1)
        competition = _DATABASE.COMPETITIONS[competition_num]["name"]
        club_num = randint(0, len(_DATABASE.CLUBS) - 1)
        club = _DATABASE.CLUBS[club_num]["name"]
        places = randint(1, 12)
        self.client.post(
            "/purchasePlaces",
            {"competition": competition, "club": club, "places": places},
        )

    @task(3)
    def logout(self):
        self.client.get("/logout")

    @task(1)
    def list_clubs(self):
        self.client.get("/clubs")


_DATABASE = _HELPER.load_db()
_HELPER.start_server()
