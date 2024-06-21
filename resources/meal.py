from flask.views import MethodView
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import MealModel
from schemas import MealDetailsSchema, QueryArgsSchema, PaginatedMealsSchema

blp = Blueprint("meal", __name__, description="Operations on meals")


@blp.route("/api/food/meal/<meal_id>")
class MealByIdResource(MethodView):

    @blp.response(200, MealDetailsSchema)
    def get(self, meal_id):
        meal = MealModel.query.get_or_404(meal_id)
        return meal

    def delete(self, meal_id):
        item = MealModel.query.get_or_404(meal_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Diet deleted."}

    def update(self, meal_id):
        item = MealModel.query.get_or_404(meal_id)
        raise NotImplementedError("Updating a meal is not implemented.")


@blp.route("/api/food/meal")
class MealResource(MethodView):

    @blp.arguments(QueryArgsSchema, location='querystring')
    @blp.response(200, PaginatedMealsSchema)
    @blp.paginate()
    def get(self, query_params, pagination_parameters):
        page_size = pagination_parameters.page_size
        page = pagination_parameters.page

        search = ''
        if "search" in query_params:
            search = query_params["search"]

        meals = MealModel.query.where(MealModel.name.like("%" + search + "%"))

        return {
            'results': meals.paginate(per_page=page_size, page=page),
            'pagination': {
                'total': meals.count(),
                'page_size': page_size,
                'page': page
            }
        }

    @blp.arguments(MealDetailsSchema)
    @blp.response(201, MealDetailsSchema)
    def post(self, meal_data):
        meal = MealModel(meal_data)

        db.session.add(meal)
        db.session.commit()

        return meal
