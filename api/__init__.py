from logging.config import dictConfig

from flask import Flask, jsonify

from api.classes.spacex import SpaceX
from api.config import config
from werkzeug.exceptions import HTTPException


def create_app(config_type: str = None) -> Flask:
    app = Flask(__name__, static_folder="../client/dist", static_url_path="/")

    if config_type is None:
        config_type = "Default"
    app.config.from_object(config[config_type])

    from api import routes

    app.register_blueprint(routes.api_bp)

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )

    app.spacex_api = SpaceX(
        base_url=app.config["BASE_URL"], ssl_verify=False, logger=app.logger
    )

    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    @app.errorhandler(404)
    def not_found():
        return app.send_static_file("index.html")

    return app
