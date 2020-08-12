from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists
from config import Config
from populate_data import get_users, get_stores, get_goods

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),  nullable=False)
    email = db.Column(db.String(),  nullable=False)
    password = db.Column(db.String(), nullable=False)


class Store(db.Model):
    __tablename__ = "stores"

    store_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),  nullable=False)
    city = db.Column(db.String(),  nullable=False)
    address = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer, nullable=True)



class Good(db.Model):
    __tablename__ = "goods"

    goods_id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(),  nullable=False)
    name = db.Column(db.String(),  nullable=False)
    price = db.Column(db.Integer(), nullable=False)


with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print("Database exist")
    else:
        print(f"Database does not exist {db.engine.url}")
        create_database(db.engine.url)
        print("Database created")


with app.app_context():
    users = get_users()
    for user in users:
        db.session.add(User(**user))
    db.session.commit()
    print("Data written in data_base successful (users)")


with app.app_context():
    stores = get_stores()
    for store in stores:
        db.session.add(Store(**store))
    db.session.commit()
    print("Data written in data_base successful (store)")


with app.app_context():
    goods = get_goods()
    for good in goods:
        db.session.add(Good(**good))
    db.session.commit()
    print("Data written in data_base successful (goods)")