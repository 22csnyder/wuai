from wuai.token_diplomacy import TokenDiplomat, Settings, post_data
from pprint import pprint
from rich import print as rprint


def assert_not_openai_api_key():
    import os
    from dotenv import load_dotenv

    load_dotenv()
    if "OPENAI_API_KEY" in os.environ:
        raise ValueError("OPENAI_API_KEY should not be defined in the environment variables.")


assert_not_openai_api_key()

td = TokenDiplomat()
token = td.token #AZURE_OPENAI_AD_TOKEN
merit = td.merit
settings = Settings()

rprint(settings)
rprint(td.merit)

import os
from openai import AzureOpenAI



# client = AzureOpenAI(
    # api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    # api_version="2024-07-01-preview",
    # azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
# )

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

deployment_name = "base-gpt-4-8k/v1/chat/completions"
# deployment_name = "base-gpt-4-8k"
deployment_name = "base-gpt-4-8k/v1/chat"

result = gpt4.chat.completions.create(
    model=deployment_name,
    messages=[{"role": "user", "content": "What is the first letter of the alphabet?"}]
)
