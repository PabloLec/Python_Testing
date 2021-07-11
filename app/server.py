from flask import Flask, render_template, request, redirect, flash, url_for
from app import database as _DATABASE
from app import helper as _HELPER

app = Flask(__name__)
app.secret_key = "something_special"

_DATABASE.load()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def show_summary():
    selected_club = _HELPER.get_club_by_mail(mail=request.form["email"])

    if selected_club:
        _HELPER.USER_CLUB = selected_club
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=_HELPER.get_future_competitions(competitions=_DATABASE.COMPETITIONS),
        )

    flash("Email address not found")
    return render_template("index.html")


@app.route("/book/<competition>/<club>")
def book(competition, club):
    selected_competition = _HELPER.get_competition_by_name(name=competition)
    selected_club = _HELPER.get_club_by_name(name=club)

    if selected_competition and selected_club:
        max_places = _HELPER.get_max_places(competition=selected_competition, club=selected_club)
        return render_template(
            "booking.html",
            club=selected_club,
            competition=selected_competition,
            max_places=max_places,
        )

    flash("Something went wrong-please try again")
    return render_template("index.html")


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = _HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = _HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = _HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )

    if purchase_is_valid:
        _DATABASE.register_purchase(
            competition=selected_competition,
            club=selected_club,
            places=places_required,
        )
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=_DATABASE.COMPETITIONS,
        )

    flash("Something went wrong-please try again")
    return render_template("index.html")


@app.route("/clubs")
def list_clubs():
    return render_template(
        "clubs.html",
        clubs=_DATABASE.CLUBS,
    )


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
