from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os
from wuai.utils import temporary_env_var  # Import the context manager

from wuai.logging_config import setup_logging
setup_logging()

td = TokenDiplomat()

import openai
openai.base_url = "https://api.openai.wustl.edu/base-gpt-4-8k/v1"

# Use the context manager to temporarily set the API key
with temporary_env_var("OPENAI_API_KEY", td.token):
    import marvin

    @marvin.fn
    def sentiment(text: str) -> float:
        """
        Returns a sentiment score for `text` 
        between -1 (negative) and 1 (positive).
        """
        
    sentiment("I love working with Marvin AI")
