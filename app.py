from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
from utilities.utils import rock_paper_scissors

def create_app():
    app = Flask(__name__)
    # client = MongoClient()
    # app.db = client.animal_game_app

    @app.route("/", methods=["GET", "POST"])
    def home():

        # need to manage list of animals, games, and outcomes
        # need to manage steps
        # add "pick your opponent" multiselection button to Home
        # add duck, panda, fox as options

        if request.method == "POST":

            animal = request.form['submit_animal']
            game = 'rock_paper_scissors'

            return redirect(url_for('faceoff', animal=animal, game=game))

        return render_template("home.html")
    

    @app.route("/about", methods=["GET"])
    def about():

        return render_template("about.html")
    

    @app.route("/faceoff/<animal>/<game>", methods=["GET", "POST"])
    def faceoff(animal, game):

        if request.method == "POST":

            choice = request.form['submit_rps']       

            return redirect(url_for('outcome', animal=animal, game=game, choice=choice))
        
        faceoff_image_path = "/static/images/faceoff_" + animal + ".png"

        return render_template("faceoff.html", faceoff_image_path=faceoff_image_path)
    

    @app.route("/outcome/<animal>/<game>/<choice>", methods=["GET", "POST"])
    def outcome(animal, game, choice):

        # placeholder
        outcome = 'You win!'

        if request.method == "POST":
            
            # POST for "Return to Home"
            return redirect(url_for('home'))

        # might want to convert to json to track outcome vs animal type and game type
        # outcome_list = []

        # need to be able to pass user's selected action
        # rps_outcome = rock_paper_scissors(1)

        return render_template("outcome.html", outcome=outcome)

    return app