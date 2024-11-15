from flask import Flask
from api.config import config


def create_app(config_type: str = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if config_type is None:
        config_type = "Default"
    app.config.from_object(config[config_type])

    from . import launches

    app.register_blueprint(launches.launches_bp)

    return app
