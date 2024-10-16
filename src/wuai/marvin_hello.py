from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os
from wuai.utils import temporary_env_var  # Import the context manager

from wuai.logging_config import setup_logging

setup_logging()

td = TokenDiplomat()

import openai

openai.base_url = "https://api.openai.wustl.edu/base-gpt-4-8k/v1"


td.refresh_token()
os.environ["OPENAI_API_KEY"] = td.token
import marvin

secret_value1 = marvin.settings.openai.api_key.get_secret_value()
print(f"{secret_value1=}")


@marvin.fn
def sentiment(text: str) -> float:
    """
    Returns a sentiment score for `text`
    between -1 (negative) and 1 (positive).
    """


sentiment("Hallo! Alles gut bei mir, danke.")

td.refresh_token()
os.environ["OPENAI_API_KEY"] = os.getenv("TEST_OPENAI_API_KEY")
# reload marvin
import importlib

importlib.reload(marvin)
secret_value2 = marvin.settings.openai.api_key.get_secret_value()
print(f"{secret_value2=}")


@marvin.fn
def sentiment(text: str) -> float:
    """
    Returns a sentiment score for `text`
    between -1 (negative) and 1 (positive).
    """


sentiment("Ich hasse es hier.")

# check OPENAI_API_KEY
print(f"{os.getenv('OPENAI_API_KEY')=}")
sentiment("I love working with Marvin AI")
