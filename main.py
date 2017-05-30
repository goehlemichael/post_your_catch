from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class catches(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   fish = db.Column(db.String(50))
   amount = db.Column(db.String(200)) 
   contact = db.Column(db.String(10))

def __init__(self, name, fish, amount, contact):
   self.name = name
   self.fish = fish
   self.amount = amount
   self.contact = contact

@app.route('/')
def show_all():
   return render_template('show_all.html', catches = catches.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['fish'] or not request.form['contact']:
         flash('Please enter all the fields', 'error')
      else:
         name = request.form['name']
         fish = request.form['fish']
         amount = request.form['amount']
         contact = request.form['contact']
         catch = catches(name=name, fish=fish, amount=amount, contact=contact)
         db.session.add(catch)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
