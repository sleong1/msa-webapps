from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class NewRecipe(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description')
    ingredients = StringField('Ingredients')
    method = StringField('Method')
    # recipe = StringField('Recipe', validators=[DataRequired()])
    favourite = BooleanField('Favourite')
    submit = SubmitField('Add')