from db import db


class ShoppingListIngredientModel(db.Model):
    __tablename__ = "shopping_list_ingredient"

    id = db.Column(db.Integer, primary_key=True)
