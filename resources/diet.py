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
