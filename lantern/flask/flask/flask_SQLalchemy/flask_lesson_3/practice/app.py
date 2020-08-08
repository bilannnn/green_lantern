from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, drop_database, database_exists
from config import Config


db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    if database_exists(db.engine.url):
        db.create_all()
        print("Database exist")
    else:
        print(f"Database does not exist {db.engine.url}")
        create_database(db.engine.url)
        print("Database created")