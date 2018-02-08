from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#用户表
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

#职位表
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    

#企业表
class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
