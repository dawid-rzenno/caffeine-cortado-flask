from db import db


class IngredientCategoryModel(db.Model):
    __tablename__ = "ingredient_category"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
