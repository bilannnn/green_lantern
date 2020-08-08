from db import db


class Store(db.Model):
    store_id = db.Column(db.Iteger, primary_key=True)
    name = db.Column(db.String)
    location = db.Colunm(db.String)
    manager = db.relationship('User', backref=db.backref('stores'))


class User(db.Model):
    user_id = db.Column(db.Iteger, primary_key=True)
    name = db.Column(db.String)
