from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import IngredientModel
from schemas import IngredientSchema, IngredientDetailsSchema, QueryArgsSchema

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
    @blp.response(200, IngredientSchema(many=True))
    def get(self, query_params):
        search = ''
        page_size = 50
        page_index = 1

        if "search" in query_params:
            search = query_params["search"]

        if "page_size" in query_params:
            page_size = query_params["page_size"]

        if "page_index" in query_params:
            page_index = query_params["page_index"]

        ingredients = (IngredientModel.query
                       .where(IngredientModel.name.like("%" + search + "%"))
                       .paginate(per_page=page_size, page=page_index))

        return ingredients

    @blp.arguments(IngredientDetailsSchema)
    @blp.response(201, IngredientDetailsSchema)
    def post(self, ingredient_data):
        ingredient = IngredientModel(**ingredient_data)

        db.session.add(ingredient)
        db.session.commit()

        return ingredient


