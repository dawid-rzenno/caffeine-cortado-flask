import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from schemas import IngredientSchema, IngredientDetailsSchema

blp = Blueprint("ingredient", __name__, description="Operations on ingredients")


@blp.route("/api/food/ingredient/<ingredient_id>")
class Ingredient(MethodView):

    @blp.response(200, IngredientDetailsSchema)
    def get(self, ingredient_id):
        return {**ingredient, "id": ingredient_id}


@blp.route("/api/food/ingredient")
class IngredientUpdate(MethodView):

    @blp.response(200, IngredientSchema(many=True))
    def get(self):
        return [{**ingredient, "id": uuid.uuid4().hex}, {**ingredient, "id": uuid.uuid4().hex}]

    @blp.arguments(IngredientSchema)
    @blp.response(201, IngredientSchema)
    def post(self, ingredient_data):
        ingredient = Ingredient(ingredient_data)

        try:
            db.session.add(ingredient)
            db.session.commit()
        except IntegrityError:
            abort(400, "Such ingredient already exist.")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding the ingredient.")

        return ingredient


