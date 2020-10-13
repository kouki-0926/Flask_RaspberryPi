import sys
sys.dont_write_bytecode=True

from flask import Flask

app=Flask(__name__)
app.config.from_object("config")

from flask_math.views import view
app.register_blueprint(view,url_prefix="/flask_math")

if __name__=="__main__":
    app.run()
