import os

from flask_cors import CORS

from api import create_app

env = os.environ.get("FLASK_ENV", "default")

app = create_app(env)
CORS(app)
