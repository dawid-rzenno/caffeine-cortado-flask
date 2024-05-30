from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request, abort

blp = Blueprint("diet", __name__, description="Operations on diets")


@blp.route("/api/food/diet/<element_id>")
class Diet(MethodView):
    def get(self, element_id):
        return {
            "id": str(element_id),
            "name": "My diet",
            "description": "A healthmaxxing diet",
            "meals": [{
                "id": "UUID",
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
            }]
        }, 200

    def post(self):
        request_data = request.get_json()
        try:
            new_meal = {
                "id": "UUID",
                "name": request_data["name"],
                "description": request_data["description"],
                "meals": request_data["meals"]
            }
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_meal, 201