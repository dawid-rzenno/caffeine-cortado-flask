from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import IngredientModel
from schemas import IngredientDetailsSchema, QueryArgsSchema, PaginatedIngredientsSchema

blp = Blueprint("ingredient", __name__, description="Operations on ingredients")


@blp.route("/api/food/ingredient/<ingredient_id>")
class IngredientByIdResource(MethodView):

    @blp.response(200, IngredientDetailsSchema)
    def get(self, ingredient_id):
        ingredient = IngredientModel.query.get_or_404(ingredient_id)
        return ingredient

    def delete(self, ingredient_id):
        item = IngredientModel.query.get_or_404(ingredient_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Diet deleted."}

    def update(self, ingredient_id):
        item = IngredientModel.query.get_or_404(ingredient_id)
        raise NotImplementedError("Updating an ingredient is not implemented.")


@blp.route("/api/food/ingredient")
class IngredientResource(MethodView):

    @blp.arguments(QueryArgsSchema, location='querystring')
    @blp.response(200, PaginatedIngredientsSchema())
    @blp.paginate()
    def get(self, query_params, pagination_parameters):

        page_size = pagination_parameters.page_size
        page = pagination_parameters.page

        search = ''
        if "search" in query_params:
            search = query_params["search"]

        ingredients = IngredientModel.query.where(IngredientModel.name.like("%" + search + "%"))

        return {
            'results': ingredients.paginate(per_page=page_size, page=page),
            'pagination': {
                'total': ingredients.count(),
                'page_size': page_size,
                'page': page
            }
        }

    @blp.arguments(IngredientDetailsSchema)
    @blp.response(201, IngredientDetailsSchema)
    def post(self, ingredient_data):
        ingredient = IngredientModel(**ingredient_data)

        db.session.add(ingredient)
        db.session.commit()

        return ingredient


