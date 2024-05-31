from db import db


class IngredientCategoryModel(db.Model):
    __tablename__ = "ingredient_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
