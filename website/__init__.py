from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    app = Flask(__name__) # Reference name of module
    app.config['SECRET_KEY'] = "helloworld"

    #Flask route
    @app.route("/")
    def home():
        return "<h1>Hello</h1>"

    return app