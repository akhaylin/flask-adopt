"""Flask app for adopt app."""

import os

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get('/')
def list_pets():
    """Renders home page, shows a list of all the pets"""

    pets = Pet.query.all()

    return render_template('pets.html', pets=pets)

@app.route("/add",methods=["GET","POST"])
def add_pet():
    """Shows the add pet form, adds pet to database then redirects home
        if user input is valid
        re-renders form if user input is invalid
    """

    form = AddPetForm()
    # print('formdata=',form.data) can loop through form.data
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes,
            available=available)

        db.session.add(pet)
        db.session.commit()

        flash("Successfully added pet!", "success")

        return redirect("/")

    return render_template("add_pet.html",form=form)


@app.route('/<int:pet_id>', methods=["GET","POST"])
def display_and_edit_pet(pet_id):
    """Shows page with pet information as well as form to edit pet info.
        On form submission with valid inputs, update pet in db
        on form submission with invalid inputs, re-render page and form
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash("Pet updated successfully!", "success")


    return render_template('display_edit_pet.html',pet=pet, form=form )

