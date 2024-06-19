from marshmallow import Schema, fields


class IngredientSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)
    amount = fields.Float(dump_only=True)
    quantity = fields.Int(dump_only=True)


class IngredientDetailsSchema(IngredientSchema):
    calories = fields.Float(required=True)
    proteins = fields.Float(required=True)
    carbohydrates = fields.Float(required=True)
    fats = fields.Float(required=True)
    price = fields.Float(required=True)


class MealSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    rating = fields.Int(required=True)


class MealDetailsSchema(MealSchema):
    ingredients = fields.List(fields.Nested(IngredientSchema()))
    ingredient_ids = fields.List(fields.Int())


class DietSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class DietDetailsSchema(DietSchema):
    meals = fields.List(fields.Nested(MealDetailsSchema()))
    meal_ids = fields.List(fields.Int())


class ShoppingListSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class ShoppingListDetailsSchema(ShoppingListSchema):
    ingredients = fields.List(fields.Nested(IngredientSchema()))
    ingredient_ids = fields.List(fields.Int())
