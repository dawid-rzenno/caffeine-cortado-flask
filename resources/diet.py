from flask.views import MethodView
from flask.views import MethodView
from flask_smorest import Blueprint

from db import db
from models import DietModel
from schemas import DietDetailsSchema, QueryArgsSchema, PaginatedDietsSchema

blp = Blueprint("diet", __name__, description="Operations on diets")


@blp.route("/api/food/diet/<diet_id>")
class DietByIdResource(MethodView):

    @blp.response(200, DietDetailsSchema)
    def get(self, diet_id):
        diet = DietModel.query.get_or_404(diet_id)
        return diet

    @blp.response(200, None)
    def delete(self, diet_id):
        item = DietModel.query.get_or_404(diet_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Diet deleted."}

    @blp.arguments(DietDetailsSchema)
    @blp.response(200, DietDetailsSchema)
    def put(self, diet_data, diet_id):

        diet: DietModel = DietModel.query.get(diet_id)

        if diet:
            diet.name = diet_data['name']
            diet.description = diet_data['description']
            diet.meals = diet_data['meals']

            status_code = 200
        else:
            diet = DietModel(diet_data)
            status_code = 201

        db.session.add(diet)
        db.session.commit()

        return diet, status_code


@blp.route("/api/food/diet")
class DietResource(MethodView):

    @blp.arguments(QueryArgsSchema, location='querystring')
    @blp.response(200, PaginatedDietsSchema)
    @blp.paginate()
    def get(self, query_params, pagination_parameters):
        page_size = pagination_parameters.page_size
        page = pagination_parameters.page

        search = ''
        if "search" in query_params:
            search = query_params["search"]

        diets = DietModel.query.where(DietModel.name.like("%" + search + "%"))

        return {
            'results': diets.paginate(per_page=page_size, page=page),
            'pagination': {
                'total': diets.count(),
                'page_size': page_size,
                'page': page
            }
        }

    @blp.arguments(DietDetailsSchema)
    @blp.response(201, DietDetailsSchema)
    def post(self, diet_data):
        diet = DietModel(diet_data)

        db.session.add(diet)
        db.session.commit()

        return diet
