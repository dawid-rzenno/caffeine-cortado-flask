from db import db


shopping_list_ingredient = db.Table(
    "shopping_list_ingredient",
    db.Column("shopping_list_id", db.Integer, db.ForeignKey('shopping_list.id'), primary_key=True),
    db.Column("ingredient_id", db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
)