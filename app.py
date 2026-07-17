"""
Application entry point.
"""

from rag.cli import CLI
from rag.config import Config


def main() -> None:
    Config.validate()
    CLI().run()


if __name__ == "__main__":
    main()
