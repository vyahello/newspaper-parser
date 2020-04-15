import pytest
from article.article import Article, _Content, _to_single_line
from tests.markers import unit

pytestmark = unit


@pytest.fixture(scope="module")
def content() -> _Content:
    yield _Content(
        html="html",
        authors="authors",
        title="title",
        text="text",
        top_image="top_image",
        videos="videos",
        keywords="keywords",
        summary="summary",
    )


@pytest.fixture(scope="module")
def article() -> Article:
    with Article("https://www.news.com.au") as article:  # type: Article
        yield article


def test_count_content(content: _Content) -> None:
    assert len(content) == 8


def test_content_to_dict(content: _Content) -> None:
    assert dict(content) == {
        "html": "html",
        "authors": "authors",
        "title": "title",
        "text": "text",
        "top_image": "top_image",
        "videos": "videos",
        "keywords": "keywords",
        "summary": "summary",
    }


def test_article_content(article: Article) -> None:
    assert isinstance(article.content(), _Content)


def test_article_as_html(article: Article) -> None:
    assert isinstance(article._as_html(), str)


def test_to_single_line() -> None:
    assert _to_single_line(("1", "2", "3")) == "1, 2, 3"
