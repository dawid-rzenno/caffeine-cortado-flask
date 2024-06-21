from marshmallow import Schema, fields


class QueryArgsSchema(Schema):
    search = fields.Str()


class PaginationSchema(Schema):
    total = fields.Int()
    page_size = fields.Int()
    page = fields.Int()


################################## INGREDIENT ###########################################


class IngredientSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    category_id = fields.Int(required=True)
    price = fields.Float(required=True)
    amount = fields.Float(dump_only=True)
    quantity = fields.Int(dump_only=True)


class PaginatedIngredientsSchema(Schema):
    pagination = fields.Nested(PaginationSchema())
    results = fields.List(fields.Nested(IngredientSchema()))


class IngredientDetailsSchema(IngredientSchema):
    calories = fields.Float(required=True)
    proteins = fields.Float(required=True)
    carbohydrates = fields.Float(required=True)
    fats = fields.Float(required=True)
    price = fields.Float(required=True)


################################## MEAL ###########################################


class MealSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    rating = fields.Int(required=True)


class PaginatedMealsSchema(Schema):
    pagination = fields.Nested(PaginationSchema())
    results = fields.List(fields.Nested(MealSchema()))


class MealDetailsSchema(MealSchema):
    ingredients = fields.List(fields.Nested(IngredientSchema()))
    ingredient_ids = fields.List(fields.Int())


################################## DIET ###########################################


class DietSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class PaginatedDietsSchema(Schema):
    pagination = fields.Nested(PaginationSchema())
    results = fields.List(fields.Nested(DietSchema()))


class DietDetailsSchema(DietSchema):
    meals = fields.List(fields.Nested(MealDetailsSchema()))
    meal_ids = fields.List(fields.Int())


################################## SHOPPING LIST ###########################################


class ShoppingListSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)


class PaginatedShoppingListsSchema(Schema):
    pagination = fields.Nested(PaginationSchema())
    results = fields.List(fields.Nested(ShoppingListSchema()))


class ShoppingListDetailsSchema(ShoppingListSchema):
    ingredients = fields.List(fields.Nested(IngredientSchema()))
    ingredient_ids = fields.List(fields.Int())
