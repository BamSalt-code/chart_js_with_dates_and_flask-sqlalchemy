from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import *


db = SQLAlchemy()

class datapoints(db.Model):
    __tablename__ = 'Graph'
    id = db.Column(db.Integer, primary_key=True)
    logged_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    calories = db.Column(db.Integer())