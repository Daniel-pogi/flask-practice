from flask import Flask, render_template

app = Flask(__name__)

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

    