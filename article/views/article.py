"""Contains API for article page views."""
from typing import Optional, Union
from flask import redirect, render_template, request, url_for
from werkzeug import Response
from article import application
from article.article import Article


@application.route(rule="/article")
def article() -> Union[Response, str]:
    """Returns parsed article content."""
    url: Optional[str] = request.args.get(key="url_to_clean")
    if not url:
        return redirect(location=url_for(endpoint="home"))

    with Article(url) as parsed_article:  # type: Article
        return render_template(
            template_name_or_list="article/index.html", article=parsed_article.content(), url=url
        )
