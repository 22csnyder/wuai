from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os

import logging
import openai

# Enable logging at the DEBUG level
openai.logger.setLevel(logging.DEBUG)

# Example: Make an OpenAI API call (Completion API)
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="What is the capital of France?",
    max_tokens=10
)
