from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request, abort

blp = Blueprint("shopping-list", __name__, description="Operations on shopping list")


@blp.route("/api/food/shopping-list/<element_id>")
class ShoppingList(MethodView):
    def get(self, element_id):
        return {
            "id": str(element_id),
            "name": "My shopping list",
            "description": "A shopping list for fitness pizza's ingredients",
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
        }

    def post(self):
        request_data = request.get_json()
        try:
            new_shopping_list = {
                "id": "UUID",
                "name": request_data["name"],
                "description": request_data["description"],
                "ingredients": request_data["ingredients"]
            }
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_shopping_list, 201