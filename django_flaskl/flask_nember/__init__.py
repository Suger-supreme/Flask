
from flask import Flask
from .views.login import lg
from .views.index import dex
def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(lg)
    app.register_blueprint(dex)
    return app