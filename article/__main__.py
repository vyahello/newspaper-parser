"""Represents executable entrypoint for `article` application."""
from article import application


def easyrun(host: str = "0.0.0.0", port: int = 5001, debug: bool = True) -> None:
    """Runs `article` application."""
    application.run(host, port, debug)


if __name__ == "__main__":
    easyrun()
