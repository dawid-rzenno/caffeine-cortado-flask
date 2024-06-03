from db import db


class DietModel(db.Model):
    __tablename__ = "diet"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
