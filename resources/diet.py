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
class DietByIdResource(MethodView):

    @blp.response(200, DietDetailsSchema)
    def get(self, diet_id):
        diet = DietModel.query.get_or_404(diet_id)
        return diet

    def delete(self, diet_id):
        item = DietModel.query.get_or_404(diet_id)
        raise NotImplementedError("Deleting a diet is not implemented.")

    def update(self, diet_id):
        item = DietModel.query.get_or_404(diet_id)
        raise NotImplementedError("Updating a diet is not implemented.")


@blp.route("/api/food/diet")
class DietResource(MethodView):

    @blp.response(200, DietSchema(many=True))
    def get(self):
        diets = DietModel.query.all()
        return diets

    @blp.arguments(DietDetailsSchema)
    @blp.response(201, DietDetailsSchema)
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
