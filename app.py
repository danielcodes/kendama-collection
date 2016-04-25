import os

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import Form
from flask_wtf.file import FileField
from wtforms import StringField
from wtforms.validators import DataRequired

from werkzeug import secure_filename

UPLOAD_FOLDER = './static/uploads/'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
    description = db.Column(db.Text())
    image = db.Column(db.String(50))

    def __init__(self, name, brand, description, image):
        self.name = name
        self.brand = brand
        self.description = description
        self.image = image 

    def __repr__(self):
        return '<Kendama %r>' % self.name


# =============================== FORMS ===============================

class KendamaForm(Form):
    name = StringField('name', validators=[DataRequired()])
    brand = StringField('brand', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    image = FileField('image')

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
        desc = form.description.data
        image = form.image.data

        # this gives the name
        filename = secure_filename(form.image.data.filename)
        # saving it to filesystem
        image.save( os.path.join(app.config['UPLOAD_FOLDER'], filename ))

        # create the object
        new_kendama = Kendama(name, brand, desc, filename)

        # add it to the db
        db.session.add(new_kendama)
        db.session.commit()

        return redirect('/')
    return render_template("kendama_form.html", form=form)


@app.route("/delete_kendama", methods=["POST"])
def delete_one():

    #the data provided from the client is just an int, the id number
    ken_id = request.json
    print request.json

    # get kendama and delete it
    '''
    ken = Kendama.query.get(ken_id)
    db.session.delete(ken)
    db.session.commit()
    '''

    return "successfully deleted kendama"


@app.route("/delete_all", methods=["POST"])
def delete_kendamas():

    Kendama.query.delete()
    db.session.commit()
    return redirect("/")

@app.route("/testing", methods=["GET"])
def testing_components():

    return render_template("dummy.html")


if __name__ == "__main__":
    app.run(debug=True)


