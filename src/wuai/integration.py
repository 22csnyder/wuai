from wuai.token_diplomacy import TokenDiplomat, Settings, post_data, get_access_token
from wuai.token_diplomacy import rprint, pprint, os

import openai


def assert_not_openai_api_key():
    import os
    from dotenv import load_dotenv

    load_dotenv()
    if "OPENAI_API_KEY" in os.environ:
        raise ValueError("OPENAI_API_KEY should not be defined in the environment variables.")


td = TokenDiplomat()
token = td.token  # AZURE_OPENAI_AD_TOKEN
merit = td.merit
settings = Settings()

rprint(settings)
rprint(td.merit)
rprint(td.payload)


# Can I set the token as the OPENAI_API_KEY? !?

rprint(td.token)
# rprint(f"{td._response=}")
rprint(td._response)

assert_not_openai_api_key()


# os.environ["OPENAI_API_KEY"] = td.token

# Set the OpenAI API key to the token from TokenDiplomat
# openai.api_key = td.token

# basic openai client
client = openai.OpenAI(api_key=td.token)


# openai key is like     sk-5Q...4hbpTx
# azure token is like    eyJ0....P1L


"""
def test_openai_client():
    client = openai.OpenAI(
        api_key=td.token,
        # api_version="2024-07-01-preview",
        # endpoint=td.api.gpt4o,
        # base_url=td.api.gpt4o,
        )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": "Hello, how are you?"}]
    )
    return response

response = test_openai_client()

rprint(response)"""


# You can now use this client to make API calls
# For example:
# response = client.chat.completions.create(
#     model="base-gpt-4-8k",
#     messages=[{"role": "user", "content": "Hello, how are you?"}]
# )


# if "azure.com" in url:
#     headers["api-key"] = TOKEN


"""
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-07-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

client = AzureOpenAI(
    azure_endpoint="https://api.openai.wustl.edu/",
    azure_ad_token=td.token,
    api_version="2024-07-01-preview",
)

result = client.chat.completions.create(
    model="base-gpt-4-8k/v1/chat/completions",
    # model="gpt-4",
    messages=[{"role": "user", "content": "What is the first letter of the alphabet?"}]
)

gpt4 = AzureOpenAI(
    azure_endpoint=td.api.gpt4,
    azure_ad_token=td.token,
    api_version="2024-07-01-preview",
)

gpt4o = AzureOpenAI(
    azure_endpoint=td.api.gpt4o,
    azure_ad_token=td.token,
    api_version="2024-07-01-preview",
)
"""


"""
# deployment_name = "base-gpt-4-8k/v1/chat/completions"
deployment_name = "base-gpt-4-8k"
# deployment_name = "base-gpt-4-8k/v1/chat"

result = gpt4.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "What is the first letter of the alphabet?"}]
)
"""
