import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import DietModel
from schemas import DietSchema, DietDetailsSchema

blp = Blueprint("diet", __name__, description="Operations on diets")


@blp.route("/api/food/diet/<diet_id>")
class Diet(MethodView):

    @blp.response(200, DietDetailsSchema)
    def get(self, diet_id):
        return {**diet, "id": diet_id}


@blp.route("/api/food/diet")
class DietUpdate(MethodView):

    @blp.response(200, DietSchema(many=True))
    def get(self):
        return [{**diet, "id": uuid.uuid4().hex}, {**diet, "id": uuid.uuid4().hex}]

    @blp.arguments(DietSchema)
    @blp.response(201, DietSchema)
    def post(self, diet_data):
        diet = DietModel(**diet_data)

        try:
            db.session.add(diet)
            db.session.commit()
        except IntegrityError:
            abort(400, "Such diet already exist.")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding the diet.")

        return diet
