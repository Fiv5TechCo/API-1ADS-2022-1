from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.controllers import default