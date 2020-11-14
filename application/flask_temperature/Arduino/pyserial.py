from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response,flash
from subprocess import getoutput
from io import BytesIO
import datetime
import serial
import os

ser=0
def init():
    global ser
    if(ser==0):
        flash("pyserial was initialized")
        ser=serial.Serial("/dev/ttyACM0",9600)
        

graph_Data=[[],[]]
def measure():
    global graph_Data
    try:
        ser.write(b'm')
    except:
        init()    
    Data=[]
    date=str(datetime.datetime.now()).split(".")
    Data.append(date[0])
    tmp_Data=[]
    for count in range(2):
        data=ser.readline()
        data=data.strip()
        data=data.decode("utf-8")
        tmp_Data.append(float(data))
    Data.append(tmp_Data)

    graph_Data[0].append(Data[0])
    graph_Data[1].append(Data[1][0]) 
    return Data

def graph_temp():
    global graph_Data
    try:
        if(len(graph_Data)>=20):
            graph_Data[0]=graph_Data[0][1:]
            graph_Data[1]=graph_Data[1][1:]

        fig=plt.figure(figsize=(9,5))
        plt.title('temperature')
        plt.xlabel("time")
        plt.xticks(rotation=45)      
        plt.ylabel("temperature [℃]")

        plt.plot(graph_Data[0],graph_Data[1])
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
    except:
        flash("graph error")

