import os
import getpass
from flask import Flask, render_template, flash

app = Flask(__name__)
app.secret_key = os.urandom(1)

user = getpass.getuser().title()

# Define a route for the app's home page
@app.route("/")
def index():
    return render_template("index.html", username=user)

# Define a route for the app's About page
@app.route("/about")
def about():
    return "<h1>This the About page</h1>"

# Define a route for the app's Contact Us page
@app.route("/contact")
def contact():
    return "<h1>This the Contact Us page</h1>"

