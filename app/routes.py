from flask import render_template
from app import app, models
import random
import getpass

AllRecipes = models.AllRecipes
user = getpass.getuser().title()

# Define a route for the app's home page
@app.route("/")
def index():
    rand_idx = []
    while len(rand_idx) < 5:
        ranval = random.randint(1, AllRecipes.query.count())
        if ranval not in rand_idx:
            rand_idx.append(ranval)
    suggested = [AllRecipes.query.filter_by(id=i).first() for i in rand_idx]
    return render_template("index.html", username=user, suggested=suggested)

# Define a route for the app's page of all recipes
@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipes=AllRecipes.query.order_by(AllRecipes.name))


# Define a route for the app's About page
@app.route("/favourites")
def favourites():
    favs = AllRecipes.query.filter_by(fav=True).all()
    return render_template("favourites.html", favs=favs)

@app.route("/recipes/<recipeid>")
def recipe(recipeid):
    this_recipe = AllRecipes.query.filter_by(id=recipeid).first()
    [ings, method] = this_recipe.recipe.split("</br></br>")
    ings = [i.strip().capitalize() for i in ings.split("</br>")]
    method = [m.strip().capitalize() for m in method.split("</br>")]
    return render_template("this_recipe.html", name=this_recipe.name, ingredients=ings, method=method)