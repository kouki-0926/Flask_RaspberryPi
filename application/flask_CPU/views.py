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
def weather_view():
    new_pref_num=request.args.get("new_pref_num")
    region=request.args.get("region")
    print(new_pref_num)
    if(new_pref_num is not None):
        weather.change_pref(new_pref_num)
        return redirect(url_for("cpu.weather_view"))
    info=weather.get_weather()
    return render_template("weather.html", Data=info[0], Forecast=info[1],region=region)
    
