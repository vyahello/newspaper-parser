"""Contains API for home page views."""
from flask import Response, render_template
from article import application
from article.status import HttpStatus


@application.route(rule="/")
@application.route(rule="/home")
@application.route(rule="/index")
def home() -> str:
    """Returns home page content."""
    return render_template(template_name_or_list="home/index.html")


@application.errorhandler(code_or_exception=HttpStatus.NOT_FOUND.code)
def not_found() -> Response:
    """Returns page not found response."""
    return Response(response="The page was not found", status=HttpStatus.NOT_FOUND.code)
