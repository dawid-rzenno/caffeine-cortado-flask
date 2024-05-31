import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from db import ingredient
from schemas import IngredientSchema

blp = Blueprint("ingredient", __name__, description="Operations on ingredients")


@blp.route("/api/food/ingredient/<ingredient_id>")
class Meal(MethodView):

    @blp.response(200, IngredientSchema)
    def get(self, ingredient_id):
        return {**ingredient, "id": ingredient_id}


@blp.route("/api/food/ingredient")
class MealUpdate(MethodView):

    @blp.arguments(IngredientSchema)
    @blp.response(201, IngredientSchema)
    def post(self, ingredient_data):
        try:
            new_ingredient = {**ingredient_data, "id": uuid.uuid4().hex}
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_ingredient
