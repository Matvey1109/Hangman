import logging
import platform
from start_game import start_game

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info(platform.python_version())
    start_game()


if __name__ == "__main__":
    main()
