from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
from flask import make_response, flash
from subprocess import getoutput
from io import BytesIO
import datetime
import serial
import os

try:
    ser = serial.Serial("/dev/ttyACM0", 9600)
    connected = True
except:
    connected = False
    print("pyserial cannot be initialized")


graph_Data = [[], [], []]


def arduino_check():
    try:
        ser.write(b'c')
        connected = True
        print("Arduino is connected")
    except:
        connected = False
        print("Arduino is not connected")



def arduino_destroy():
    if(connected):
        ser.close()
        print("pyserial destroy")
    else:
        print("pyserial cannot close")


def reset_graph_Data():
    if(connected):
        global graph_Data
        graph_Data = [[], [], []]
        print("graph_Data was initialized")


def measure_temp():
    if(connected):
        global graph_Data
        Data = []
        ser.write(b'm')

        date = datetime.datetime.now()
        display_date = str(date).split(".")
        Data.append(display_date[0])
        graph_date = date.strftime("%H:%M:%S")
        graph_Data[0].append(graph_date)

        tmp_Data = []
        for count in range(2):
            data = ser.readline()
            data = data.strip()
            data = data.decode("utf-8")
            tmp_Data.append(float(data))
        Data.append(tmp_Data)
        graph_Data[1].append(tmp_Data[0])
        graph_Data[2].append(tmp_Data[1])

        print("measure_temp was successful")
        return Data


def graph_temp(graph_type):
    global graph_Data
    try:
        if(len(graph_Data[0]) != len(graph_Data[1])):
            graph_Data = [[], [], []]
        if(len(graph_Data[0]) >= 20):
            graph_Data[0] = graph_Data[0][1:]
            graph_Data[1] = graph_Data[1][1:]
            graph_Data[2] = graph_Data[2][1:]

        fig = plt.figure(figsize=(7, 8))
        plt.xlabel("time")
        plt.xticks(rotation=60)

        if(graph_type == "temp"):
            plt.title('temperature')
            plt.ylabel("temperature [℃]")
            plt.plot(graph_Data[0], graph_Data[1])
        elif(graph_type == "humi"):
            plt.title('humidity')
            plt.ylabel("humidity [%]")
            plt.plot(graph_Data[0], graph_Data[2])

        # canvasにプロットした画像を出力
        canvas = FigureCanvasAgg(fig)
        png_output = BytesIO()
        canvas.print_png(png_output)
        data = png_output.getvalue()
        # HTML側に渡すレスポンスを生成する
        response = make_response(data)
        response.headers['Content-Type'] = 'image/png'
        response.headers['Content-Length'] = len(data)
        return response
    except:
        flash("graph error")


def LED(state):
    ser.write(state.encode("utf-8"))
    s = ser.readline()
    s = s.strip()
    return s.decode("utf-8")
