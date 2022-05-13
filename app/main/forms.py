from flask_wtf import FlaskForm #import wtf module

from wtforms import StringField, TextAreaField, SubmitField #for the text field, textarea filed and submit button
from wtforms.validators import DataRequired #prevent from submision without input values

class ReviewForm(FlaskForm):

    title = StringField('Review Title', validators=[DataRequired()]) #firstt parameter is the label. the second is the validation
    review = TextAreaField('Movie Revies', validators = [DataRequired()])
    submit= SubmitField('Submit')