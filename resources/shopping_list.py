from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import ShoppingListModel
from schemas import ShoppingListSchema, ShoppingListDetailsSchema

blp = Blueprint("shopping-list", __name__, description="Operations on shopping list")


@blp.route("/api/food/shopping-list/<shopping_list_id>")
class ShoppingListByIdResource(MethodView):

    @blp.response(200, ShoppingListDetailsSchema)
    def get(self, shopping_list_id):
        shopping_list = ShoppingListModel.query.get_or_404(shopping_list_id)
        return shopping_list

    def delete(self, shopping_list_id):
        item = ShoppingListModel.query.get_or_404(shopping_list_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Diet deleted."}

    def update(self, shopping_list_id):
        item = ShoppingListModel.query.get_or_404(shopping_list_id)
        raise NotImplementedError("Updating a shopping list is not implemented.")


@blp.route("/api/food/shopping-list")
class ShoppingListResource(MethodView):

    @blp.response(200, ShoppingListSchema(many=True))
    def get(self):
        shopping_lists = ShoppingListModel.query.all()
        return shopping_lists

    @blp.arguments(ShoppingListDetailsSchema)
    @blp.response(201, ShoppingListDetailsSchema)
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
