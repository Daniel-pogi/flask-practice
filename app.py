from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Note(db.Model):
    id = Column(Integer, primary_key=True)
    data = Column(String, nullable=False)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html')

@app.route('/add')
def add():
    return render_template('pages/add.html')

@app.route('/delete')
def delete():
    return render_template('pages/delete.html')

@app.route('/update')
def update():
    return render_template('pages/update.html')

    