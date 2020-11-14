from apscheduler.schedulers.background import BackgroundScheduler
import sys
sys.dont_write_bytecode = True
from flask import Flask

from flask_CPU.CPU.CPU import update_CPU
from flask_math.views import Math
from flask_CPU.views import cpu
from flask_temperature.views import temp
from main.views import main

sched = BackgroundScheduler(standalone=True, coalesce=True)
sched.add_job(update_CPU, 'interval', minutes=10)
sched.start()

app=Flask(__name__)
app.config.from_object("config")

app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")
app.register_blueprint(temp,url_prefix="/flask_temp")

if __name__=="__main__":
    # app.run()
    app.run("0.0.0.0",port=5000)
