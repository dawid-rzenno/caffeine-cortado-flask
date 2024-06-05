from marshmallow import Schema, fields


class IngredientSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    ingredient_category_id = fields.Int(required=True)
    price = fields.Float(required=True)


class IngredientDetailsSchema(IngredientSchema):
    amount = fields.Float(required=True)
    quantity = fields.Int(required=True)
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
    ingredients = fields.List(fields.Nested(IngredientDetailsSchema()))


class DietSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class DietDetailsSchema(DietSchema):
    meals = fields.List(fields.Nested(MealDetailsSchema()))


class ShoppingListSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    ingredients = fields.List(fields.Nested(IngredientSchema()))


class ShoppingListDetailsSchema(ShoppingListSchema):
    ingredients = fields.List(fields.Nested(IngredientDetailsSchema()))
