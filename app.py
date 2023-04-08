from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
from utilities.utils import rock_paper_scissors

def create_app():
    app = Flask(__name__)
    # client = MongoClient()
    # app.db = client.animal_game_app

    @app.route("/", methods=["GET"])
    def home():

        # need to manage list of animals, games, and outcomes
        # need to manage steps
        # add "pick your opponent" multiselection button to Home
        # add duck, panda, fox as options

        entries = [1,2,3]

        return render_template("home.html", entries=entries)
    
    @app.route("/about", methods=["GET"])
    def about():

        entries = [1,2,3]

        return render_template("about.html", entries=entries)
    
    @app.route("/faceoff/<animal>/<game>", methods=["GET", "POST"])
    def faceoff(animal, game):

        if request.method == "POST":

            if request.form['submit_rps'] in ['rock', 'paper', 'scissors']:

                print('YES')

            else:

                print('NO')   

            # need to capture user selection and pass to variable             

            return redirect(url_for('home'))

        return render_template("faceoff.html")
    
    @app.route("/outcome/<animal>/<game>", methods=["GET"])
    def outcome(animal, game):
        
        # placeholder
        outcome = 'You win!'

        # might want to convert to json to track outcome vs animal type and game type
        outcome_list = []

        # need to be able to pass user's selected action
        rps_outcome = rock_paper_scissors(1)

        return render_template("outcome.html", outcome=outcome)

    return app