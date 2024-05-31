from db import db


class ShoppingListModel(db.Model):
    __tablename__ = "shopping_list"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)
