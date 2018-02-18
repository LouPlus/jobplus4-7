from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    

class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
    

class Company(db.Model):
	id = db.Column(db.Integer, primary_key=True)
