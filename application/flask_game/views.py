from flask import request, redirect, url_for, render_template, flash, Blueprint, session
from flask_game.Game import *

game = Blueprint("game", __name__,
                 template_folder='templates_game', static_folder="static_game")


@game.route("/")
def index_view():
    return render_template("index_game.html")


@game.route("/janken")
def janken_view():
    n = request.args.get("n")
    type = request.args.get("type")
    if(type == "ml"):
        if(n == '1' or n == '2' or n == '3'):
            Anser = janken_ml.janken_ml(int(n), session.get('result_ml', 'aaa'))
            session['result_ml'] = Anser[2]
            print(session.get('result_ml', 'aaa'))
            return render_template("janken.html", type=type, n=Anser[0][0], nc=Anser[0][1], Anser=Anser[1])
        elif(n == "init"):
            session['result_ml'] = [0, 0, 0]
            return render_template("janken.html", type=type)
        elif(n == "reset"):
            session['result_ml'] = [0, 0, 0]
            flash("正常に勝敗結果が初期化されました")
            return render_template("janken.html", type=type)
        else:
            return redirect(url_for("game.janken_view", type="ml", n="init"))
    elif(type == "rm"):
        if(n == '1' or n == '2' or n == '3'):
            Anser = janken.janken(int(n), session.get('result_rm', 'aaa'))
            session['result_rm'] = Anser[2]
            print(session.get('result_ml', 'aaa'))
            return render_template("janken.html", type=type, n=Anser[0][0], nc=Anser[0][1], Anser=Anser[1])
        elif(n == "init"):
            session['result_rm'] = [0, 0, 0]
            return render_template("janken.html", type=type)
        elif(n == "reset"):
            session['result_rm'] = [0, 0, 0]
            flash("正常に勝敗結果が初期化されました")
            return render_template("janken.html", type=type)
        else:
            return redirect(url_for("game.janken_view", type="rm", n="init"))
    else:
        return redirect(url_for("game.janken_view", type="rm", n="init"))


@game.route("/box")
def box_view():
    return render_template("box.html")


@game.route("/bike")
def bike_view():
    return render_template("bike.html")
