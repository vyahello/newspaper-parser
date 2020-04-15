"""Represents executable entrypoint for `article` application."""
from dataclasses import dataclass
from article import application


@dataclass
class Server:
    """A server entrypoint setup."""

    host: str = "0.0.0.0"
    port: int = 5001
    debug: bool = True


def easyrun(server: Server) -> None:
    """Runs `article` application.

    Args:
        server (Server): a server entrypoint
    """
    application.run(server.host, server.port, server.debug)


if __name__ == "__main__":
    easyrun(server=Server())
