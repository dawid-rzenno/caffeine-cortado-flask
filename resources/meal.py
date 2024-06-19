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

    @blp.response(200, MealSchema(many=True))
    def get(self):
        meals = MealModel.query.all()
        return meals

    @blp.arguments(MealDetailsSchema)
    @blp.response(201, MealDetailsSchema)
    def post(self, meal_data):
        meal = MealModel(meal_data)

        db.session.add(meal)
        db.session.commit()

        return meal
