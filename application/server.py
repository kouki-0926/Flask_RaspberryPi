import sys
sys.dont_write_bytecode = True
from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

from main.views import main
from flask_math.views import Math
from flask_CPU.views import cpu
from flask_arduino.views import arduino
from flask_raspi.views import raspi
from flask_game.views import game

app.register_blueprint(main)
app.register_blueprint(Math, url_prefix="/math")
app.register_blueprint(cpu, url_prefix="/CPU")
app.register_blueprint(arduino, url_prefix="/arduino")
app.register_blueprint(raspi, url_prefix="/raspi")
app.register_blueprint(game,url_prefix="/game")

from apscheduler.schedulers.background import BackgroundScheduler
from flask_CPU.CPU.CPU import update_CPU
from flask_arduino.Arduino.pyserial import measure_temp
from flask_raspi.raspi.raspi import gpio_setup, gpio_destroy

sched = BackgroundScheduler(standalone=True, coalesce=True)
sched.add_job(update_CPU, 'interval', minutes=1)
sched.add_job(measure_temp, 'interval', minutes=1)
sched.start()

if __name__ == "__main__":
    try:
        update_CPU()
        measure_temp()
        gpio_setup()
        app.run("0.0.0.0", port=5000)
    except KeyboardInterrupt:
        gpio_destroy()
