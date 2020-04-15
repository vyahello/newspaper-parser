from typing import Sequence
import pytest
from flask.wrappers import Response
from flask.testing import Client, FlaskClient
from article import application
from article.status import HttpStatus
from tests.markers import functional

pytestmark = functional


@pytest.fixture(scope="module")
def client() -> Client:
    with FlaskClient(application) as client:  # type: Client
        yield client


@pytest.fixture(scope="module")
def empty_article_request(client: Client) -> Sequence[str]:
    yield client.get("/article", buffered=True)


@pytest.fixture(scope="module")
def filled_article_request(client: Client) -> Sequence[str]:
    yield client.get("/article?url_to_clean=https://www.news.com.au", buffered=True)


@pytest.mark.parametrize("route", ("/", "/index", "/home"))
def test_home_status(client: Client, route: str) -> None:
    assert str(HttpStatus.SUCCESS) in client.get(route, buffered=True)[1]


@pytest.mark.parametrize("route", ("/", "/index", "/home"))
def test_home_title(client: Client, route: str) -> None:
    assert "Newspaper Parser" in str(client.get(route, buffered=True)[0][0])


def test_empty_article_status(empty_article_request: Sequence[str]) -> None:
    assert str(HttpStatus.REDIRECTED) in empty_article_request[1]


def test_filled_article_status(filled_article_request: Sequence[str]) -> None:
    assert str(HttpStatus.SUCCESS) in filled_article_request[1]


def test_empty_article_title(empty_article_request: Sequence[str]) -> None:
    assert "Redirecting" in str(empty_article_request[0][0])


def test_filled_article_title(filled_article_request: Sequence[str]) -> None:
    assert "Extracted Data" in str(filled_article_request[0][0])


def test_not_found() -> None:
    with application.test_client() as client:  # type: Client
        response: Response = client.get("/not_found")
        assert response.status_code == HttpStatus.NOT_FOUND.code
        assert response.data == b"The page was not found"
