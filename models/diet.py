from db import db
from models import MealModel
from models.diet_meal import diet_meal


class DietModel(db.Model):
    __tablename__ = "diet"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    meals = db.relationship("MealModel", secondary=diet_meal, backref="diets")

    def __init__(self, request_data: dict):
        if request_data.get('id'):
            self.id = request_data.get('id')

        self.name = request_data.get('name')
        self.description = request_data.get('description')

        if request_data.get('meals'):
            self.meals = [MealModel(meal) for meal in request_data.get('meals')]
