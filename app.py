from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient()
    app.db = client.animal_game_app

    @app.route("/", methods=["GET"])
    def home():

        entries = [1,2,3]

        return render_template("home.html", entries=entries)
    
    @app.route("/about", methods=["GET"])
    def about():

        entries = [1,2,3]

        return render_template("about.html", entries=entries)
    
    @app.route("/faceoff/<animal>/<game>", methods=["GET", "POST"])
    def faceoff(animal, game):
        
        entries = [1,2,3]

        return render_template("faceoff.html", entries=entries)

    return app