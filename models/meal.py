from db import db
from models import IngredientModel


class MealModel(db.Model):
    __tablename__ = "meal"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Details
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    ingredients = db.relationship("MealIngredient")

    def __init__(self, request_data: dict):
        if request_data.get('id'):
            self.id = request_data.get('id')

        self.name = request_data.get('name')
        self.description = request_data.get('description')
        self.rating = request_data.get('rating')

        ingredient_ids = request_data.get('ingredient_ids')

        self.ingredients = []
        if ingredient_ids:
            for ingredient_id in ingredient_ids:
                ingredient = IngredientModel.query.get_or_404(ingredient_id)
                self.ingredients.append(ingredient)


