from flask import Flask, render_template, request, redirect, url_for
from utilities.utils import rock_paper_scissors, ret_faceoff_text, ret_outcome_text

def create_app():

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home():

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

        faceoff_text = ret_faceoff_text(animal)

        return render_template("faceoff.html", faceoff_image_path=faceoff_image_path, faceoff_text=faceoff_text)
    

    @app.route("/outcome/<animal>/<game>/<choice>", methods=["GET", "POST"])
    def outcome(animal, game, choice):

        if request.method == "POST":

            return redirect(url_for('home'))

        rps_outcome = rock_paper_scissors(choice)

        rps_status = rps_outcome['status']

        outcome_image_path = "/static/images/outcome_" + animal + "_rps_" + rps_status + ".png"

        outcome_text = ret_outcome_text(animal, rps_status)

        return render_template("outcome.html", outcome_image_path=outcome_image_path, outcome_text=outcome_text)

    return app