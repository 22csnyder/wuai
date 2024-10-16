from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os
from wuai.utils import assert_not_openai_api_key, temporary_openai_api_key  # Updated import path
from wuai.logging_config import setup_logging

from openai.types.chat import ChatCompletion


messages = [{"role": "user", "content": "Hey! Was geht ab?"}]


td = TokenDiplomat()
assert td.token
assert_not_openai_api_key()


"""
This code works without having to specify the model, it uses a hook to rewrite the path to the correct endpoint.
"""

#####   EXAMPLE   #####
import openai

# Can I set the token as the OPENAI_API_KEY? !?
setup_logging()
import http.client as httplib

httplib.HTTPConnection.debuglevel = 1

gpt4o_model = "base-gpt-4o-128k"
gpt4_model = "base-gpt-4-8k"


# --------- hook?

# https://github.com/openai/openai-python/issues/547
import httpx
from openai import OpenAI

model = gpt4_model
version = "v1"
relative_endpoint = f"/{model}/{version}"
rprint(f"{relative_endpoint=}")


def update_base_url(request: httpx.Request) -> None:
    # rewrite the path segment to what the proxy expects
    rprint(request.url, type(request.url))
    rprint(request.url.path)

    # new_path = "/oops" + request.url.path
    new_endpoint = relative_endpoint + request.url.path
    rprint(f"{new_endpoint=}")
    request.url = request.url.copy_with(path=new_endpoint)


# ----------

client = openai.OpenAI(
    base_url=f"https://api.openai.wustl.edu/",
    api_key=td.token,
    http_client=httpx.Client(
        event_hooks={
            "request": [update_base_url],
        }
    ),
)


response: ChatCompletion = client.chat.completions.create(
    model='I think this doesnt matter',
    messages=messages,
)

rprint(response.choices[0].message.content)

#####   EXAMPLE   #####
