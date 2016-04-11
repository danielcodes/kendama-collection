from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.secret_key = 'ZC4dti6GaxOikyVy0uy3T5XVEwSkmtZD'

# =============================== MODELS ===============================
# taken from the basic app, so db is created in this same dir
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI 

db = SQLAlchemy(app)

class Kendama(db.Model):
    # link has to be validated as a url in the form
    # Name | Brand | Link | Description
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    brand = db.Column(db.String(50))
    link = db.Column(db.String(100))
    description = db.Column(db.Text())

    def __init__(self, name, brand, link, description):
        self.name = name
        self.brand = brand
        self.link = link
        self.description = description

    def __repr__(self):
        return '<Kendama %r>' % self.name


# =============================== FORMS ===============================

class KendamaForm(Form):
    name = StringField('name', validators=[DataRequired()])
    brand = StringField('brand', validators=[DataRequired()])
    link = StringField('link', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])


# =============================== VIEWS ===============================

@app.route("/")
def home():

    kendamas = Kendama.query.all() 

    return render_template("kendamas.html", kendamas=kendamas) 


@app.route("/kendamas")
def kendama_list():
    return "Hey, you currently have no kendamas"


@app.route("/add_kendama", methods=["GET", "POST"])
def new_kendama():

    form = KendamaForm()

    if form.validate_on_submit():
        # access from content with form.name.data
        # create new kendama and place it in the database
        name = form.name.data
        brand = form.brand.data
        link = form.link.data
        desc = form.description.data

        # create the object
        new_kendama = Kendama(name, brand, link, desc)

        # add it to the db
        db.session.add(new_kendama)
        db.session.commit()

        return redirect('/')
    return render_template("kendama_form.html", form=form)


@app.route("/testing", methods=["GET", "POST"])
def testing_components():

    form = KendamaForm()
    print "hey, testing page"
    if form.validate_on_submit():
        # access from content with form.name.data
        # create new kendama and place it in the database
        name = form.name.data
        brand = form.brand.data
        link = form.link.data
        desc = form.description.data

        # create the object
        new_kendama = Kendama(name, brand, link, desc)

        # add it to the db
        db.session.add(new_kendama)
        db.session.commit()

        return redirect('/')
    return render_template("dummy.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)


