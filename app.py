from flask import Flask, render_template
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
    return render_template("base.html") 


@app.route("/kendamas")
def kendama_list():
    return "Hey, you currently have no kendamas"


@app.route("/add_kendama")
def new_kendama():

    return render_template("kendama_form.html")

@app.route("/testing")
def testing_components():

    form = KendamaForm()

    return render_template("dummy.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)


