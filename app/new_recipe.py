from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewRecipe(FlaskForm):
    name = StringField('Dish name', validators=[DataRequired()])
    description = StringField('Description')
    recipe = StringField('Recipe', validators=[DataRequired()])
    fav = BooleanField('Favourite')
    submit = SubmitField('Sign In')