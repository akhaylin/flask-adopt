from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, AnyOf, URL, Optional

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField(
        "Pet name:",
        validators=[InputRequired()])

   
    species = SelectField(
        "Species:",
        choices=[('dog','Dog'),('cat','Cat'),('porcupine','Porcupine')],
        validators=[AnyOf(values=['dog','cat','porcupine'])])

    photo_url = StringField(
        "Photo URL:",
         validators=[URL(require_tld=False),
         Optional()])

    age = SelectField(
        'Age',
        choices=[('baby','Baby'),
        ('young','Young'),
        ('adult','Adult'),
        ('senior','Senior')],
        validators=[AnyOf(values=['baby','young','adult', 'senior'])])

    ##TODO:research length validator with min max
    notes = TextAreaField("Notes:", validators=[Optional()])



class EditPetForm(FlaskForm):
    """Form for editing pets"""

    photo_url = StringField(
        "Photo URL:",
         validators=[URL(require_tld=False),
         Optional()])

    notes = TextAreaField(
        "Notes:",
         validators=[Optional()])

    available = BooleanField('Is Pet Available?')