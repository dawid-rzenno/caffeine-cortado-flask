from flask.views import MethodView
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import ShoppingListModel
from schemas import ShoppingListDetailsSchema, PaginatedShoppingListsSchema, QueryArgsSchema

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

    @blp.arguments(QueryArgsSchema, location='querystring')
    @blp.response(200, PaginatedShoppingListsSchema)
    @blp.paginate()
    def get(self, query_params, pagination_parameters):
        page_size = pagination_parameters.page_size
        page = pagination_parameters.page

        search = ''
        if "search" in query_params:
            search = query_params["search"]

        shopping_lists = ShoppingListModel.query.where(ShoppingListModel.name.like("%" + search + "%"))

        return {
            'results': shopping_lists.paginate(per_page=page_size, page=page),
            'pagination': {
                'total': shopping_lists.count(),
                'page_size': page_size,
                'page': page
            }
        }

    @blp.arguments(ShoppingListDetailsSchema)
    @blp.response(201, ShoppingListDetailsSchema)
    def post(self, shopping_list_data):
        shopping_list = ShoppingListModel(shopping_list_data)

        db.session.add(shopping_list)
        db.session.commit()

        return shopping_list
