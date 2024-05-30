from flask import request, abort
from flask.views import MethodView
from flask_smorest import Blueprint

blp = Blueprint("meal", __name__, description="Operations on meals")


@blp.route("/api/food/meal/<element_id>")
class Meal(MethodView):
    def get(self, element_id):
        return {
            "id": str(element_id),
            "name": "Pizza",
            "description": "A healthy pizza",
            "ingredients": [{
                "id": "UUID",
                "name": "Secret ingredient",
                "category": 0,
                "price": 20,
                "count": 1,
                "amount": 0.725,
                "calories": 750,
                "proteins": 100,
                "carbohydrates": 500,
                "fats": 250
            }]
        }, 200

    def post(self):
        request_data = request.get_json()
        try:
            new_meal = {
                "id": None,
                "name": request_data["name"],
                "description": request_data["description"],
                "ingredients": request_data["ingredients"]
            }
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_meal, 201