from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import path
from .routes import API

database = SQLAlchemy()
database_name = "SpaceSheep.db"

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{database_name}'
    database.init_app(app)
    CORS(app)
    
    create_database(app)
    app.register_blueprint(API, url_prefix = "/")
    
    

    return app

def create_database(app):
    if not path.exists('website/' + database_name):
        database.create_all(app=app)
        print('Created Database!')