"""Package contains a set of interfaces to operate `article` application."""
from flask import Flask

__author__: str = "Volodymyr Yahello"
__email__: str = "vyahello@gmail.com"
__version__: str = "0.0.1"

application: Flask = Flask(__name__)

from .views import article, home  # noqa: F401, E402
