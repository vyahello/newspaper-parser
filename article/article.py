"""Contains interfaces to manipulate articles."""
from dataclasses import dataclass
from types import TracebackType
from typing import Generator, Optional, Sequence, Tuple, Type
from xml.etree import ElementTree
from punish.style import AbstractStyle
import newspaper


def _to_single_line(sequence: Sequence[str], separator_as_forward: str = ", ") -> str:
    """Coverts sequence if items into single line.

    Args:
        sequence (Sequence[str): an iterable
        separator_as_forward (str): a separator item
    """
    return separator_as_forward.join(sequence)


@dataclass
class _Content:
    """Represents article content."""

    html: str
    authors: str
    title: str
    text: str
    top_image: str
    videos: str
    keywords: str
    summary: str

    def __len__(self) -> int:
        """Returns count of items."""
        return len(self.__dict__)

    def __iter__(self) -> Generator[Tuple[str, str], None, None]:
        """Returns iter_mapped content as a dictionary."""
        yield from self.__dict__.items()


class Article(AbstractStyle):
    """Represents parsed article.

    Implemented as a context manager.
    """

    def __init__(self, url: str) -> None:
        self._article: newspaper.Article = newspaper.Article(url)

    def __enter__(self) -> "Article":
        """Returns article itself."""
        self._article.download()
        self._article.parse()
        return self

    def content(self) -> _Content:
        """Returns parsed article."""
        return _Content(
            html=self._as_html(),
            authors=_to_single_line(self._article.authors),
            title=self._article.title,
            text=self._article.text,
            top_image=self._article.top_image,
            videos=_to_single_line(self._article.movies),
            keywords=_to_single_line(self._article.keywords),
            summary=self._article.summary,
        )

    def _as_html(self) -> str:
        """Returns article as `html` content."""
        try:
            return str(ElementTree.tostring(element=self._article.clean_top_node))
        except newspaper.ArticleException:
            return "Error occurred while converting html to string."

    def __exit__(  # noqa: U100
        self,
        exception_type: Optional[Type[BaseException]],
        exception_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        """Exits from article."""
        del self
