from subprocess import getoutput
import datetime
import os

def measure_CPU():
    time=nowtime()
    temp=measure_temp()
    clock=measure_clock()
    volt=measure_volt()
    arm=measure_arm()
    gpu=measure_gpu()
    return [time,temp,clock,volt,arm,gpu]

Time,Temp,Clock,Volt,Arm,Gpu=[],[],[],[],[],[]
def nowtime():
    time=str(datetime.datetime.now()).split(".")
    time2=time[0].split(" ")
    Time.append(time2[1])
    return time[0]

def measure_temp():
    temp=getoutput("vcgencmd measure_temp").split('=')
    temp=temp[1].split("'")
    Temp.append(float(temp[0]))
    return "Temperature: "+temp[0]+"℃"

def measure_clock():
    clock=getoutput("vcgencmd measure_clock arm").split("=")
    clock=float(clock[1])/10**9
    Clock.append(clock)
    return "clock: "+str(clock)+"GHz"

def measure_volt():
    volt=str(getoutput("vcgencmd measure_volts")).split("=")
    volt=volt[1].split("V")
    Volt.append(float(volt[0]))
    return "volt: "+volt[0]+"V"
    
def measure_arm():
    arm=getoutput("vcgencmd get_mem arm").split("=")
    arm=arm[1].split("M")
    Arm.append(int(arm[0]))
    return "arm: "+arm[0]+"MB"

def measure_gpu():
    gpu=getoutput("vcgencmd get_mem gpu").split("=")
    gpu=gpu[1].split("M")
    Gpu.append(int(gpu[0]))
    return "gpu: "+gpu[0]+"MB"


def measure_CPU2(graph_type):
    global Time,Temp,Clock,Volt,Arm,Gpu
    if(graph_type=="temp"):
        Data=Temp
    elif(graph_type=="clock"):
        Data=Clock
    elif(graph_type=="volt"):
        Data=Volt
    elif(graph_type=="arm"):
        Data=Arm
    elif(graph_type=="gpu"):
        Data=Gpu
    
    if(len(Time)!=len(Data)):
        Time,Temp,Clock,Volt,Arm,Gpu=[],[],[],[],[],[]

    if(len(Time)>=30):
        Time=Time[1:]
        Data=Data[1:]

    return [Time,Data]

