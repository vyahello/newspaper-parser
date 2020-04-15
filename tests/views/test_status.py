from article.status import HttpStatus
from tests.markers import unit

pytestmark = unit


def test_status() -> None:
    assert isinstance(HttpStatus.NOT_FOUND, HttpStatus)


def test_status_code() -> None:
    assert HttpStatus.NOT_FOUND.code == 404
