"""Package contains a set of interfaces to operate `article` application."""
from flask import Flask
from .views import home

__author__: str = "Volodymyr Yahello"
__email__: str = "vyahello@gmail.com"
__version__: str = "0.0.0"

application: Flask = Flask(__name__)
application.register_blueprint(home.to_register)
