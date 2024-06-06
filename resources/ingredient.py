from flask import abort
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import IngredientModel
from schemas import IngredientSchema, IngredientDetailsSchema

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

    @blp.response(200, IngredientSchema(many=True))
    def get(self):
        ingredients = IngredientModel.query.all()
        return ingredients

    @blp.arguments(IngredientDetailsSchema)
    @blp.response(201, IngredientDetailsSchema)
    def post(self, ingredient_data):
        ingredient = IngredientModel(ingredient_data)

        try:
            db.session.add(ingredient)
            db.session.commit()
        except IntegrityError:
            abort(400, "Such ingredient already exist.")
        except SQLAlchemyError:
            abort(500, "An error occurred while adding the ingredient.")

        return ingredient


