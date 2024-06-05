from db import db


diet_meal = db.Table(
    "diet_meal",
    db.Column("diet_id", db.Integer, db.ForeignKey('diet.id')),
    db.Column("meal_id", db.Integer, db.ForeignKey('meal.id'))
)
