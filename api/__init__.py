from logging.config import dictConfig
from werkzeug.exceptions import HTTPException
from flask import Flask, jsonify

from api.classes.spacex import SpaceX
from api.config import config


def create_app(config_type: str = None) -> Flask:
    app = Flask(__name__, static_folder="../client/dist", static_url_path="/")

    if config_type is None:
        config_type = "Default"
    app.config.from_object(config[config_type])

    from api.index import index
    from api.launches import launches

    app.register_blueprint(launches.launches_bp)
    app.register_blueprint(index.index_bp)

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

    @app.errorhandler(404)
    def no_data_found(error):
        return jsonify("Request returned no results"), 404

    @app.errorhandler(Exception)
    def handle_exception(error):
        if isinstance(error, HTTPException):
            # Create a response
            response = error.get_response()
            response.data = jsonify(
                {
                    "code": error.code,
                    "name": error.name,
                    "description": error.description,
                }
            ).data
            response.content_type = "application/json"
            return response

        return (
            jsonify(
                "Unknown error occurred, please contact API developers for assistance"
            ),
            500,
        )

    return app
