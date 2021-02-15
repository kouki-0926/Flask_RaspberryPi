from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_raspberryPi.raspberryPi.raspberryPi import Blink

raspberryPi = Blueprint("raspberryPi", __name__, template_folder='templates_raspberryPi', static_folder="static_raspberryPi")


@raspberryPi.route("/")
def index_view():
    return render_template("index_raspberryPi.html")


@raspberryPi.route("/Blink", methods=["GET", "POST"])
def Blink_view():
    try:
        Blink()
        return render_template("raspberryPi.html")
    except:
        flash("Error")
        return redirect(url_for("raspberryPi.index_view"))