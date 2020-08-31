from flask import render_template
from app import app, models
import random
import getpass

app.secret_key = os.urandom(1)

AllRecipes = models.AllRecipes
user = getpass.getuser().title()

# Define a route for the app's home page
@app.route("/")
def index():
    rand_idx = [random.randint(0, AllRecipes.query(Name).count()) for i in range(5)]
    suggested = [AllRecipes.query.all()[i] for i in rand_idx]
    return render_template("index.html", username=user, suggested=suggested)

# Define a route for the app's page of all recipes
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


# Define a route for the app's About page
@app.route("/favourites")
def favourites():
    return render_template("favourites.html")

