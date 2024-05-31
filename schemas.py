from marshmallow import Schema, fields


class IngredientSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Int(required=True)
    price = fields.Float(required=True)
    quantity = fields.Int(required=True)
    amount = fields.Float(required=True)
    calories = fields.Float(required=True)
    proteins = fields.Float(required=True)
    carbohydrates = fields.Float(required=True)
    fats = fields.Float(required=True)


class MealSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    rating = fields.Int(required=True)
    ingredients = fields.List(fields.Nested(IngredientSchema()))


class DietSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    meals = fields.List(fields.Nested(MealSchema()))


class ShoppingListSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    ingredients = fields.List(fields.Nested(IngredientSchema()))