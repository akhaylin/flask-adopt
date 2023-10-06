from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet name:",validators=[InputRequired()])
    species = StringField("Species:",validators=[InputRequired()])
    photo_url = StringField("Photo URL:")
    age = SelectField('Age',choices=[
        ('baby','Baby'),
        ('young','Young'),
        ('adult','Adult'),
        ('senior','Senior')
        ])
    notes = TextAreaField("Notes:")
    available = BooleanField('Is Pet Available?')