import os
from flask import Flask
from config import get_config
from typing import Optional
from app.views.home import home as home_bp


def create_app(config_name: Optional[str] = None) -> Flask:
    app = Flask(__name__)
    if config_name is None:
        config_name = os.getenv("FLASK_ENV")

    # TODO: Overwrite config values with those in environment variables if present
    app.config.from_object(get_config(config_name))
    app.register_blueprint(home_bp)

    return app
