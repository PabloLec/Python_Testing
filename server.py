from flask import Flask, render_template, request, redirect, flash, url_for
import database as DATABASE
import helper as HELPER

app = Flask(__name__)
app.secret_key = "something_special"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def show_summary():
    selected_club = HELPER.get_club_by_mail(mail=request.form["email"])

    if selected_club:
        HELPER.USER_CLUB = selected_club
        return render_template(
            "welcome.html",
            club=HELPER.USER_CLUB,
            competitions=DATABASE.COMPETITIONS,
        )

    flash("Email address not found")
    return render_template("index.html")


@app.route("/book/<competition>/<club>")
def book(competition, club):
    selected_competition = HELPER.get_competition_by_name(name=competition)
    selected_club = HELPER.get_club_by_name(name=club)

    if selected_competition and selected_club:
        max_places = HELPER.get_max_places(competition=selected_competition, club=selected_club)
        return render_template(
            "booking.html",
            club=selected_club,
            competition=selected_competition,
            max_places=max_places,
        )

    flash("Something went wrong-please try again")
    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=DATABASE.COMPETITIONS,
    )


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():

    selected_competition = HELPER.get_competition_by_name(name=request.form["competition"])
    selected_club = HELPER.get_club_by_name(name=request.form["club"])
    places_required = request.form["places"]

    purchase_is_valid = HELPER.is_purchase_valid(
        competition=selected_competition,
        club=selected_club,
        places=places_required,
    )

    if purchase_is_valid:
        DATABASE.register_purchase(
            competition=selected_competition,
            club=selected_club,
            places=places_required,
        )
        flash("Great-booking complete!")
        return render_template(
            "welcome.html",
            club=selected_club,
            competitions=DATABASE.COMPETITIONS,
        )

    flash("Something went wrong-please try again")
    return render_template(
        "welcome.html",
        club=HELPER.USER_CLUB,
        competitions=DATABASE.COMPETITIONS,
    )


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
