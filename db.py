import uuid

ingredient = {
    "id": uuid.uuid4().hex,
    "name": "Secret ingredient",
    "category": 0,
    "price": 20,
    "count": 1,
    "amount": 0.725,
    "calories": 750,
    "proteins": 100,
    "carbohydrates": 500,
    "fats": 250
}

meal = {
    "id": uuid.uuid4().hex,
    "name": "Pizza",
    "description": "A healthy pizza",
    "ingredients": [ingredient]
}

diet = {
    "id": uuid.uuid4().hex,
    "name": "My diet",
    "description": "A healthmaxxing diet",
    "meals": [meal]
}

shopping_list = {
    "id": uuid.uuid4().hex,
    "name": "My shopping list",
    "description": "A shopping list for fitness pizza's ingredients",
    "ingredients": [ingredient]
}
