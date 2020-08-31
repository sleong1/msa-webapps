from flask import render_template
from app import app, models

AllRecipes = models.AllRecipes

@app.route('/')
def index():
    title = 'My Recipe Book'
    recipes = AllRecipes.query.all()
    return render_template("index.html", title=title, recipes=recipes)