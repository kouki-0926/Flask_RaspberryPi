import requests
from flask import redirect,request,url_for,render_template,flash,Blueprint,make_response
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask_CPU.CPU import *

cpu=Blueprint("cpu",__name__,template_folder='templates_cpu',static_folder="static_cpu")

@cpu.route("/")
def index():
    return render_template("index_cpu.html")

@cpu.route("/measure",methods=["GET","POST"])
def measure():
    Data=CPU.measure_CPU()
    if(request.method=="GET"):
        graph_type=request.args.get("graph_type")
    elif(request.method=="POST"):
        graph_type=request.form.get("graph_type")
    return render_template("measure.html",Data=Data,graph_type=graph_type)



@cpu.route('/graph.png')
def graph():
    graph_type=request.args.get("graph_type")

    fig=plt.figure(figsize=(9,8))
    plt.xlabel("time")
    plt.xticks(rotation=45)

    if(graph_type=="temp"):
        plt.title('temperature')
        plt.ylabel("temperature [℃]")
    elif(graph_type=="clock"):
        plt.title('clock')
        plt.ylabel("clock [GHz]")
    elif(graph_type=="volt"):
        plt.title('volt')
        plt.ylabel("volt [v]")
    elif(graph_type=="arm"):
        plt.title('arm')
        plt.ylabel("arm [MB]")
    elif(graph_type=="gpu"):
        plt.title('gpu')
        plt.ylabel("gpu [MB]")


    Data=CPU.measure_CPU2(graph_type)
    plt.plot(Data[0],Data[1])
    # canvasにプロットした画像を出力
    canvas=FigureCanvasAgg(fig)
    png_output=BytesIO()
    canvas.print_png(png_output)
    data=png_output.getvalue()
    # HTML側に渡すレスポンスを生成する
    response=make_response(data)
    response.headers['Content-Type']='image/png'
    response.headers['Content-Length']=len(data)
    return response

@cpu.route("/weather",methods=["GET","POST"])
def weather():
    url = "https://weather.tsukumijima.net/api/forecast"
    payload = {"city": "120010"}
    data = requests.get(url, params=payload).json()

    Data=[]

    title = "{}予報です".format(data["title"])
    Data.append(title)
    Forecast=[]

    for i in range(0, 3, 1):
        forecast=[]
        date="{} {}".format(data["forecasts"][i]["dateLabel"], data["forecasts"][1]["date"])
        forecast.append(date)

        try:
            max_temp="最高気温{}℃".format(data["forecasts"][i]["temperature"]["max"]["celsius"])
        except:
            max_temp="最高気温{}℃".format("null")
        forecast.append(max_temp)   

        try:
            min_temp="最低気温{}℃".format(data["forecasts"][i]["temperature"]["min"]["celsius"])
        except:
            min_temp="最低気温{}℃".format("null")
        forecast.append(min_temp)    

        forecast.append("0時から6時までの降水確率   {}".format(data["forecasts"][i]["chanceOfRain"]["00-06"]))
        forecast.append("6時から12時までの降水確率  {}".format(data["forecasts"][i]["chanceOfRain"]["06-12"]))
        forecast.append("12時から18時までの降水確率 {}".format(data["forecasts"][i]["chanceOfRain"]["12-18"]))
        forecast.append("18時から24時までの降水確率 {}".format(data["forecasts"][i]["chanceOfRain"]["18-24"]))
        Forecast.append(forecast)

    Data.append("{}".format(data["publicTime_format"]))
    Data.append("{}".format(data["description"]["text"]))
    Data.append("{}".format(data["copyright"]["link"]))
    Data.append("{}".format(data["copyright"]["provider"][0]["link"]))

    Data.append("{}".format(data["forecasts"][0]["image"]["url"]))

    return render_template("weather.html", Data=Data, Forecast=Forecast)


