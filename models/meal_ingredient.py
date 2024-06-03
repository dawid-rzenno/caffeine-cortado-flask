from db import db


class MealIngredientModel(db.Model):
    __tablename__ = "meal_ingredient"

    id = db.Column(db.Integer, primary_key=True)
    