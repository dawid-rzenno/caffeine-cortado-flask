from db import db


class DietMealModel(db.Model):
    __tablename__ = "diet_meal"

    id = db.Column(db.Integer, primary_key=True)
