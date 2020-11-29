from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
import sys
sys.dont_write_bytecode=True

from main.views import main
from flask_math.views import Math
from flask_CPU.views import cpu
from flask_arduino.views import arduino

from flask_CPU.CPU.CPU import update_CPU
from flask_arduino.Arduino.pyserial import measure_temp

sched=BackgroundScheduler(standalone=True,coalesce=True)
sched.add_job(update_CPU,'interval',minutes=10)
sched.add_job(measure_temp,'interval',minutes=10)
sched.start()

app=Flask(__name__)
app.config.from_object("config")

app.register_blueprint(main)
app.register_blueprint(Math,url_prefix="/flask_math")
app.register_blueprint(cpu,url_prefix="/flask_CPU")
app.register_blueprint(arduino,url_prefix="/flask_arduino")

if __name__=="__main__":
    update_CPU()
    measure_temp()
    # app.run()
    app.run("0.0.0.0",port=5000)
