import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint

from db import diet
from schemas import DietSchema

blp = Blueprint("diet", __name__, description="Operations on diets")


@blp.route("/api/food/diet/<diet_id>")
class Diet(MethodView):

    @blp.response(200, DietSchema)
    def get(self, diet_id):
        return {**diet, "id": diet_id}


@blp.route("/api/food/diet")
class DietUpdate(MethodView):

    @blp.arguments(DietSchema)
    @blp.response(201, DietSchema)
    def post(self, diet_data):
        try:
            new_diet = {**diet_data, "id": uuid.uuid4().hex}
        except KeyError:
            abort(400, message="Invalid parameters")

        return new_diet


@blp.route("/api/food/diet/all")
class Diets(MethodView):

    @blp.response(200, DietSchema(many=True))
    def get(self):
        return [{**diet, "id": uuid.uuid4().hex}, {**diet, "id": uuid.uuid4().hex}]
