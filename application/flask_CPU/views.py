from flask import redirect, request, url_for, render_template, flash, Blueprint
from flask_CPU.CPU import *

cpu = Blueprint("cpu", __name__, template_folder='templates_cpu', static_folder="static_cpu")


@cpu.route("/")
def index_view():
    return render_template("index_cpu.html")


@cpu.route("/measure", methods=["GET", "POST"])
def measure_view():
    try:
        Data = CPU.get_display_Data()
        if(Data[0] == "Error"):
            flash("Error:CPU情報の取得失敗")
            return redirect(url_for("cpu.index_view"))
        if(request.method == "GET"):
            graph_type = request.args.get("graph_type")
        elif(request.method == "POST"):
            graph_type = request.form.get("graph_type")
        return render_template("measure.html", Data=Data, graph_type=graph_type)
    except:
        flash("Error:CPU情報の取得失敗")
        return redirect(url_for("cpu.index_view"))


@cpu.route('/graph.png')
def graph_view():
    graph_type = request.args.get("graph_type")
    return CPU.graph_cpu(graph_type)


@cpu.route("/weather")
def weather_view():
    pref_num = request.args.get("pref_num")
    if(pref_num is None):
        return redirect(url_for("cpu.weather_view", pref_num="130010"))

    try:
        Data = weather.get_weather(pref_num)
        return render_template("weather.html", Data=Data, pref_num=pref_num)
    except:
        flash("ERROR")
        return redirect(url_for("cpu.index_view"))


@cpu.route("/ip_address")
def ip_address_view():
    ip_address = request.args.get("ip_address")
    if(ip_address is not None):
        Data = ip.get_location(ip_address)
        try:
            st_Data = station.get_data(Data["longitude"], Data["latitude"])
        except:
            st_Data = []
            flash("最寄り駅の情報取得失敗")
        return render_template("ip_address.html", Data=Data, st_Data=st_Data, init_flag=0)
    else:
        return render_template("ip_address.html", Data=[], st_Data=[], init_flag=1)
