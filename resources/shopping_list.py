import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from db import shopping_list
from schemas import ShoppingListSchema, ShoppingListDetailsSchema

blp = Blueprint("shopping-list", __name__, description="Operations on shopping list")


@blp.route("/api/food/shopping-list/<shopping_list_id>")
class ShoppingList(MethodView):

    @blp.response(200, ShoppingListDetailsSchema)
    def get(self, shopping_list_id):
        return {"id": shopping_list_id, **shopping_list}


@blp.route("/api/food/shopping-list")
class ShoppingListUpdate(MethodView):

    @blp.response(200, ShoppingListSchema(many=True))
    def get(self):
        return [{**shopping_list, "id": uuid.uuid4().hex}, {**shopping_list, "id": uuid.uuid4().hex}]

    @blp.arguments(ShoppingListSchema)
    @blp.response(201, ShoppingListSchema)
    def post(self, shopping_list_data):
        try:
            new_shopping_list = {**shopping_list_data, "id": uuid.uuid4().hex}
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_shopping_list
