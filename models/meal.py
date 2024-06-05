from db import db
from models import IngredientModel
from models.meal_ingredient import meal_ingredient


class MealModel(db.Model):
    __tablename__ = "meal"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    ingredients = db.relationship("IngredientModel", secondary=meal_ingredient, backref="meals")

    def __init__(self, request_data: dict):
        if request_data.get('id'):
            self.id = request_data.get('id')

        self.name = request_data.get('name')
        self.description = request_data.get('description')
        self.rating = request_data.get('rating')

        if request_data.get('ingredients'):
            self.ingredients = [IngredientModel(**ingredient) for ingredient in request_data.get('ingredients')]
