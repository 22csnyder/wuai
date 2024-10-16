from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os
from wuai.utils import assert_not_openai_api_key, temporary_openai_api_key  # Updated import path
from wuai.logging_config import setup_logging
from openai.types.chat import ChatCompletion


#####WORKING EXAMPLE#####

import openai

# Can I set the token as the OPENAI_API_KEY? !?
setup_logging()

td = TokenDiplomat()
assert td.token
assert_not_openai_api_key()

gpt4o_model = "base-gpt-4o-128k"

messages = [{"role": "user", "content": "Hey! Was geht ab?"}]

client = openai.OpenAI(
    base_url="https://api.openai.wustl.edu/base-gpt-4o-128k/v1",
    api_key=td.token,
)
response = client.chat.completions.create(
    # model="baseXXX",
    model="base-gpt-4o-128k",
    messages=messages,
)

rprint(response.choices[0].message.content)

#####WORKING EXAMPLE#####


"""
# deployment_name = "base-gpt-4-8k/v1/chat/completions"
deployment_name = "base-gpt-4-8k"
# deployment_name = "base-gpt-4-8k/v1/chat"

result = gpt4.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "What is the first letter of the alphabet?"}]
)
"""
