from db import db


meal_ingredient = db.Table(
    "meal_ingredient",
    db.Column("meal_id", db.Integer, db.ForeignKey('meal.id'), primary_key=True),
    db.Column("ingredient_id", db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
)
