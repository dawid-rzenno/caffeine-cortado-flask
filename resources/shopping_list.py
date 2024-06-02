import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import ShoppingListModel
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
        shopping_list = ShoppingListModel(shopping_list_data)

        try:
            db.session.add(shopping_list)
            db.session.commit()
        except IntegrityError:
            abort(400, "Such shopping list already exist.")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding the shopping list.")

        return shopping_list
