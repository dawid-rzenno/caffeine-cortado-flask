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
class MealByIdResource(MethodView):

    @blp.response(200, MealDetailsSchema)
    def get(self, meal_id):
        meal = MealModel.query.get_or_404(meal_id)
        return meal

    def delete(self, diet_id):
        item = MealModel.query.get_or_404(diet_id)
        raise NotImplementedError("Deleting a meal is not implemented.")

    def update(self, diet_id):
        item = MealModel.query.get_or_404(diet_id)
        raise NotImplementedError("Updating a meal is not implemented.")


@blp.route("/api/food/meal")
class MealResource(MethodView):

    @blp.response(200, MealSchema(many=True))
    def get(self):
        meals = MealModel.query.all()
        return meals

    @blp.arguments(MealDetailsSchema)
    @blp.response(201, MealDetailsSchema)
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
