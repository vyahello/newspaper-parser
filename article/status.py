"""Contains interfaces to work with application statuses."""
from enum import Enum


class HttpStatus(Enum):
    """Represents http status code item."""

    NOT_FOUND: int = 404

    @property
    def code(self) -> int:
        """Returns value of status code."""
        return self.value
