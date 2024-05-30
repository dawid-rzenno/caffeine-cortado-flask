from flask import Flask
from flask_smorest import Api

from resources.meal import blp as meal_blueprint
from resources.diet import blp as diet_blueprint
from resources.shopping_list import blp as shopping_list_blueprint

app = Flask(__name__)


app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Caffeinated Server REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)
api.register_blueprint(meal_blueprint)
api.register_blueprint(diet_blueprint)
api.register_blueprint(shopping_list_blueprint)
