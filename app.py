import os
import getpass
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = os.urandom(1)

user = getpass.getuser().title()

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("index.html", username=user)

# Define a route for the app's page of all recipes
@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


# Define a route for the app's About page
@app.route("/favourites")
def favourites():
    return "<h1>This are your favourite recipes</h1>"


## Code for logging in
# @app.route('/login',  methods=["GET", "POST"])
# def login():
#     """The view for the login page"""
#     try:
#         error = ''
#         if request.method == "POST":
#             attempted_username = request.form['username']
#             attempted_password = request.form['password']
#             if attempted_username == 'admin' and attempted_password == os.environ['USER_PASSWORD']:
#                 session['logged_in'] = True
#                 session['username'] = request.form['username']
#                 return redirect(url_for('edit_database', city_id=city_id))
#             else:
#                 print('invalid credentials')
#                 error = 'Invalid credentials. Please, try again.'
#         return render_template('login.html', error=error, city_name=city_record.city_name, city_id=city_id)
#     except Exception as e:
#         return render_template('login.html', error=str(e), city_name=city_record.city_name, city_id=city_id)


# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         """login session"""
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             pass
#         return redirect(url_for('login'))
#     return wrap