from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

def create_app():
    app = Flask(__name__)
    client = MongoClient()
    app.db = client.user_data_app

    @app.route("/", methods=["GET"])
    def home():

        entries = [1,2,3]

        return render_template("home.html", entries=entries)
    
    return app