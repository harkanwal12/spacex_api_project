from logging.config import dictConfig

from flask import Flask

from api.classes.spacex import SpaceX
from api.config import config


def create_app(config_type: str = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

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

    return app
