from db import db


class IngredientModel(db.Model):
    __tablename__ = "ingredient"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    calories = db.Column(db.Float, nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    carbohydrates = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    ingredient_category_id = db.Column(db.Integer, db.ForeignKey("ingredient_category.id"), unique=False, nullable=False)
