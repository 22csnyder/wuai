import logging
from rich.logging import RichHandler


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,  # Set the logging level
        format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
        handlers=[
            logging.FileHandler("openai_requests.log"),  # Log file path
            RichHandler(),  # Rich console handler
        ],
    )
    import openai

    # Set up OpenAI client logging
    http_client_logger = logging.getLogger("openai")
    http_client_logger.setLevel(logging.DEBUG)

    # openai.logger.setLevel(logging.DEBUG)
