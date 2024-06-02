import uuid
from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import MealModel
from schemas import MealSchema, MealDetailsSchema

blp = Blueprint("meal", __name__, description="Operations on meals")


@blp.route("/api/food/meal/<meal_id>")
class Meal(MethodView):

    @blp.response(200, MealDetailsSchema)
    def get(self, meal_id):
        return {**meal, "id": meal_id}


@blp.route("/api/food/meal")
class MealUpdate(MethodView):

    @blp.response(200, MealSchema(many=True))
    def get(self):
        return [{**meal, "id": uuid.uuid4().hex}, {**meal, "id": uuid.uuid4().hex}]

    @blp.arguments(MealSchema)
    @blp.response(201, MealSchema)
    def post(self, meal_data):
        meal = MealModel(meal_data)

        try:
            db.session.add(meal)
            db.session.commit()
        except IntegrityError:
            abort(400, "Such meal already exist.")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding the meal.")

        return meal
