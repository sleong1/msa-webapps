from flask import render_template, request
from flask import jsonify, redirect
from app import app, models, db
from app.forms import NewRecipe
import random
import getpass

AllRecipes = models.AllRecipes
user = getpass.getuser().title()

# Define a route for the app's home page
@app.route("/", methods=['FAV', 'GET'])
def index():
    suggested = new_suggested([])
    return render_template("index.html", username=user, suggested=suggested)

# Define a route for the app's page of all recipes
@app.route("/recipes")
def recipes():
    return render_template("recipes.html", recipes=AllRecipes.query.order_by(AllRecipes.name))


# Define a route for the app's About page
@app.route("/favourites", methods=['FAV', 'GET'])
def favourites():
    favs = AllRecipes.query.filter_by(fav=True).all()
    return render_template("favourites.html", favs=favs)

@app.route("/recipes/<recipeid>", methods=['FAV', 'GET', 'REMOVE'])
def recipe(recipeid):
    if request.method == 'FAV':
        fav_change(recipeid)
    if request.method == 'REMOVE':
        delete_recipe(recipeid)
        return redirect("/recipes")

    this_recipe = AllRecipes.query.filter_by(id=recipeid).first()
    ings = [i.strip().capitalize() for i in this_recipe.ingredients.split("</br>")]
    method = [m.strip().capitalize() for m in this_recipe.method.split("</br>")]
    return render_template("this_recipe.html", name=this_recipe.name, ingredients=ings, method=method, fav=this_recipe.fav, id=recipeid)


@app.route("/new-recipe", methods=['POST', 'GET'])
def newRecipe():
    form = NewRecipe(request.form)

    if request.method == "POST": # and form.validate():
        recipe = AllRecipes()
        save_new_recipe(form)
        return redirect("/recipes")

    return render_template("new_recipe.html", form=form)

@app.route('/recipes/<recipeid>/edit', methods=['GET', 'POST'])
def editRecipe(recipeid):
    recipedata = AllRecipes.query.get(recipeid)
    form = NewRecipe(formdata=request.form, obj=recipedata)

    if request.method == 'POST':
        save_edit(recipeid, form)
        return redirect('/recipes/' + str(recipeid))

    return render_template('edit_recipe.html', form=form, name=recipedata.name)

def save_edit(recipeid, form):
    data = AllRecipes.query.get(recipeid)
    
    data.name = form.name.data
    data.description = form.description.data
    data.ingredients = form.ingredients.data
    data.method = form.method.data
    data.fav = form.favourite.data
    
    db.session.commit()


def save_new_recipe(form):
    name = form.name.data
    description = form.description.data
    ingredients = form.ingredients.data
    method = form.method.data
    recipe = ingredients + "</br></br>" + method
    fav = form.favourite.data

    new_recipe = AllRecipes(name=name, description=description, ingredients=ingredients, method=method, fav=fav)
    db.session.add(new_recipe)
    db.session.commit()

def fav_change(recipeid):
    recipedata = AllRecipes.query.get(recipeid)
    if recipedata != None:
        msg = {
            'message': 'Favourite toggle successful'
        }
        recipedata.fav = not recipedata.fav
        db.session.commit()
        return jsonify(msg), 200
    msg = {
        'message': 'Recipe not found'
    }
    return jsonify(msg), 204

def new_suggested(rand_idx=[]):
    while len(rand_idx) < 5:
        ranval = random.randint(1, AllRecipes.query.count())
        if ranval not in rand_idx:
            rand_idx.append(ranval)
    return [AllRecipes.query.filter_by(id=i).first() for i in rand_idx]


def delete_recipe(recipeid):
    recipedata = AllRecipes.query.get(recipeid)
    if recipedata != None:
        msg = {
            'message': 'Delete successful'
        }
        db.session.delete(recipedata)
        db.session.commit()
        return jsonify(msg), 200
    msg = {
        'message': 'Recipe not found'
    }
    return jsonify(msg), 204
