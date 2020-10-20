import requests
import datetime

init_flag=1
old_minute=0
Data,Forecast=[],[]

def get_weather():
    global init_flag,old_minute,Data,Forecast
    dt_now=datetime.datetime.now()
    now_minute=dt_now.minute

    if(init_flag==1):
        old_minute=now_minute-20
        init_flag=0
    
    if(now_minute-old_minute<20):
        return [Data,Forecast]
    else:
        print("update Data")
        Data, Forecast=[],[]
        old_minute=now_minute

        url="https://weather.tsukumijima.net/api/forecast"
        payload={"city": "120010"}
        data=requests.get(url,params=payload).json()
        #地点　0
        Data.append("{}予報です".format(data["title"]))
        for i in range(0, 3, 1):
            forecast=[]
            #日付　0
            forecast.append("{} {}".format(data["forecasts"][i]["dateLabel"], data["forecasts"][i]["date"]))
            #天気　1
            forecast.append("{}".format(data["forecasts"][i]["telop"]))
            #天気アイコン　2
            forecast.append("{}".format(data["forecasts"][i]["image"]["url"]))
            #最高気温  3
            try:
                forecast.append("最高気温{}℃".format(data["forecasts"][i]["temperature"]["max"]["celsius"]))
            except:
                forecast.append("最高気温{}℃".format("null"))
            #最低気温　4
            try:
                forecast.append("最低気温{}℃".format(data["forecasts"][i]["temperature"]["min"]["celsius"]))
            except:
                forecast.append("最低気温{}℃".format("null"))
            #降水確率  5~8
            forecast.append("0時から6時までの降水確率   {}".format(data["forecasts"][i]["chanceOfRain"]["00-06"]))
            forecast.append("6時から12時までの降水確率  {}".format(data["forecasts"][i]["chanceOfRain"]["06-12"]))
            forecast.append("12時から18時までの降水確率 {}".format(data["forecasts"][i]["chanceOfRain"]["12-18"]))
            forecast.append("18時から24時までの降水確率 {}".format(data["forecasts"][i]["chanceOfRain"]["18-24"]))
            Forecast.append(forecast)
        #時刻  1
        Data.append("{}".format(data["publicTime_format"]))
        #天気予報  2,3
        description=str(data["description"]["text"]).split("<天気変化等の留意点>")
        Data.append("{}".format(description[0]))
        Data.append("<天気変化等の留意点> {}".format(description[1]))
        #copyright link 4
        Data.append("{}".format(data["copyright"]["link"]))
        #copyrught 画像  5
        Data.append("{}".format(data["copyright"]["image"]["url"]))
        #気象庁 url  6
        Data.append("{}".format(data["copyright"]["provider"][0]["link"]))
        return [Data,Forecast]



