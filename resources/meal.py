import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from db import meal
from schemas import MealSchema

blp = Blueprint("meal", __name__, description="Operations on meals")


@blp.route("/api/food/meal/<meal_id>")
class Meal(MethodView):

    @blp.response(200, MealSchema)
    def get(self, meal_id):
        return {**meal, "id": meal_id}


@blp.route("/api/food/meal")
class MealUpdate(MethodView):

    @blp.arguments(MealSchema)
    @blp.response(201, MealSchema)
    def post(self, meal_data):
        try:
            new_meal = {**meal_data, "id": uuid.uuid4().hex}
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_meal
