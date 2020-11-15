from flask import redirect,url_for,render_template,flash,Blueprint
from flask_temperature.Arduino import pyserial as pys

temp=Blueprint("temp",__name__,template_folder='templates_temp',static_folder="static_temp")

@temp.route("/")
def index_view():
    return render_template("index_temp.html")

@temp.route("/measure")
def measure_view():
    try:
        Data=pys.measure()
        return render_template("measure_temp.html",time=Data[0],temperature=Data[1][0],humidity=Data[1][1])
    except:
        return redirect(url_for(measure_view))

@temp.route("/graph_temp")
def graph_temp_view():
    return pys.graph_temp()
