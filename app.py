from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Note(db.Model):
    id = Column(Integer, primary_key=True)
    data = Column(Text, nullable=False)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/sampledb"
db.init_app(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template('pages/home.html')

@app.route('/add', methods=["POST", "GET"])
def add():
    if request.method == "POST":
        note = request.form.get("note")
        data = Note(data=note)
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('add'))
    data = Note.query.all()

    return render_template('pages/add.html', data=data)

@app.route('/delete')
def delete():
    return render_template('pages/delete.html')

@app.route('/update')
def update():
    return render_template('pages/update.html')

    