import sys
sys.dont_write_bytecode=True

from flask import Flask

app=Flask(__name__)
app.config.from_object("config")

from main.views import main
app.register_blueprint(main)

from flask_math.views import view
app.register_blueprint(view,url_prefix="/flask_math")

from flask_CPU.views import cpu
app.register_blueprint(cpu,url_prefix="/flask_CPU")

if __name__=="__main__":
    app.run("0.0.0.0",port=5000)
