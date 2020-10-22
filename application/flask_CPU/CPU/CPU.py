from subprocess import getoutput
import datetime
import os

display_Data=[]
graph_Data=[[],[],[],[],[],[]]
def measure_CPU():
    update_CPU()
    return display_Data

def update_CPU():
    print("update cpu")
    global display_Data
    display_Data=[]
    display_Data.append(nowtime())
    display_Data.append(measure_temp())
    display_Data.append(measure_clock())
    display_Data.append(measure_volt())
    display_Data.append(measure_arm())
    display_Data.append(measure_gpu())

def nowtime():
    time=str(datetime.datetime.now()).split(".")
    time2=time[0].split(" ")
    graph_Data[0].append(time2[1])
    return time[0]

def measure_temp():
    temp=getoutput("vcgencmd measure_temp").split('=')
    temp=temp[1].split("'")
    graph_Data[1].append(float(temp[0]))
    return "Temperature: "+temp[0]+"℃"

def measure_clock():
    clock=getoutput("vcgencmd measure_clock arm").split("=")
    clock=float(clock[1])/10**9
    graph_Data[2].append(clock)
    return "clock: "+str(clock)+"GHz"

def measure_volt():
    volt=str(getoutput("vcgencmd measure_volts")).split("=")
    volt=volt[1].split("V")
    graph_Data[3].append(float(volt[0]))
    return "volt: "+volt[0]+"V"
    
def measure_arm():
    arm=getoutput("vcgencmd get_mem arm").split("=")
    arm=arm[1].split("M")
    graph_Data[4].append(int(arm[0]))
    return "arm: "+arm[0]+"MB"

def measure_gpu():
    gpu=getoutput("vcgencmd get_mem gpu").split("=")
    gpu=gpu[1].split("M")
    graph_Data[5].append(int(gpu[0]))
    return "gpu: "+gpu[0]+"MB"


def measure_CPU2(graph_type):
    global graph_Data
    if(len(graph_Data[0])>30):
        for i in range(len(graph_Data)):
            graph_Data[i]=graph_Data[i][1:]

    if(graph_type=="temp"):
        return [graph_Data[0],graph_Data[1]]
    elif(graph_type=="clock"):
        return [graph_Data[0],graph_Data[2]]
    elif(graph_type=="volt"):
        return [graph_Data[0],graph_Data[3]]
    elif(graph_type=="arm"):
        return [graph_Data[0],graph_Data[4]]
    elif(graph_type=="gpu"):
        return [graph_Data[0],graph_Data[5]]

