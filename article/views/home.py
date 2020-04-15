"""Contains API for home page views."""
from flask import Response, blueprints as bprint, render_template
from article.status import HttpStatus

to_register: bprint.Blueprint = bprint.Blueprint(name=__name__, import_name=__name__)


@to_register.route(rule="/")
@to_register.route(rule="/index")
def home() -> str:
    """Returns home page content."""
    return render_template(template_name_or_list="home/index.html")


@to_register.errorhandler(code_or_exception=HttpStatus.NOT_FOUND.code)
def not_found() -> Response:
    """Returns page not found response."""
    return Response(response="The page was not found", status=HttpStatus.NOT_FOUND.code)
