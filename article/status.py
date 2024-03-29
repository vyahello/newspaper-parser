"""Contains interfaces to work with application statuses."""
from enum import Enum


class HttpStatus(Enum):
    """Represents http status code item."""

    SUCCESS: int = 200
    REDIRECTED: int = 302
    NOT_FOUND: int = 404

    @property
    def code(self) -> int:
        """Returns value of status code."""
        return self.value

    def __str__(self) -> str:
        """Returns code as a string representation."""
        return str(self.value)
