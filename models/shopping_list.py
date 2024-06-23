from db import db
from models import IngredientModel
from models.shopping_list_ingredient import shopping_list_ingredient


class ShoppingListModel(db.Model):
    __tablename__ = "shopping_list"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Details
    price = db.Column(db.Float, nullable=False)
    ingredients = db.relationship("IngredientModel", secondary=shopping_list_ingredient, backref="shopping_lists")

    def __init__(self, request_data: dict):
        if request_data.get('id'):
            self.id = request_data.get('id')

        self.name = request_data.get('name')
        self.description = request_data.get('description')

        ingredient_ids = request_data.get('ingredient_ids')

        self.ingredients = []
        if ingredient_ids:
            for ingredient_id in ingredient_ids:
                self.ingredients.append(IngredientModel.query.get_or_404(ingredient_id))

