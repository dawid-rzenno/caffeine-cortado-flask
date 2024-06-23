from db import db
from models import MealModel
from models.diet_meal import diet_meal


class DietModel(db.Model):
    __tablename__ = "diet"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, nullable=False)

    # Details
    price = db.Column(db.Float, nullable=False)
    meals = db.relationship("MealModel", secondary=diet_meal, backref="diets")

    def __init__(self, request_data: dict):
        self.update(request_data)

    def update(self, request_data: dict):
        if request_data.get('id'):
            self.id = request_data.get('id')

        self.name = request_data.get('name')
        self.description = request_data.get('description')

        meal_ids = request_data.get('meal_ids')

        self.meals = []
        if meal_ids:
            for meal_id in meal_ids:
                self.meals.append(MealModel.query.get_or_404(meal_id))
