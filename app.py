import os

from flask import Flask
from flask_cors import CORS
from flask_smorest import Api

from db import db

from resources.meal import blp as meal_blueprint
from resources.diet import blp as diet_blueprint
from resources.ingredient import blp as ingredient_blueprint
from resources.shopping_list import blp as shopping_list_blueprint


def create_app(db_url="postgresql+psycopg2://postgres:example@192.168.0.100:5432/fitness"):
    app = Flask(__name__)

    app.__version__ = '0.4.0'

    CORS(app)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Caffeinated Server REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(ingredient_blueprint)
    api.register_blueprint(meal_blueprint)
    api.register_blueprint(diet_blueprint)
    api.register_blueprint(shopping_list_blueprint)

    return app
