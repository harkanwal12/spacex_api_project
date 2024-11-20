from logging.config import dictConfig

from flask import Flask

from api.classes.spacex import SpaceX
from api.config import config


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

    # Serves the react app from flask as a static file
    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    # Handles the re-routing when directly accessing front-end endpoints
    # The front-end routes do not exist on flask so a 404 is thrown
    # This catches the 404 and re-routes back to react-router
    @app.errorhandler(404)
    def error_404(e):
        return app.send_static_file("index.html")

    return app
