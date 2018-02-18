from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()




class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    

class Company(db.Model):
	id = db.Column(db.Integer, primary_key=True)
