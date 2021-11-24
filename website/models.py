from . import db
from sqlalchemy.sql import func


class Customer(db.Model):
    celular=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(150))

