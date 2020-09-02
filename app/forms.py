from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired


class NewRecipe(FlaskForm):
    name = StringField('Dish name', validators=[DataRequired()])
    description = StringField('Description')
    ingredients = TextAreaField('Ingredients', render_kw={"rows": 10, "cols": 75}, validators=[DataRequired()])
    method = TextAreaField('Method', render_kw={"rows": 20, "cols": 150}, validators=[DataRequired()])
    # recipe = StringField('Recipe', validators=[DataRequired()])
    favourite = BooleanField('Favourite')
    submit = SubmitField('Add')