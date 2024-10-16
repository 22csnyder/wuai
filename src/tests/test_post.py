"""Debug what happens on a requests.post level when openai.chat.Completions is called"""

import openai
from openai.types.chat import ChatCompletion
from wuai.logging_config import setup_logging
from wuai.utils import temporary_openai_api_key, assert_not_openai_api_key  # Updated import path

# Configure logging
setup_logging()

def openai_chat() -> ChatCompletion:
    response: ChatCompletion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hey! Was geht ab?"}]
    )
    return response

# Ensure the API key is not set in the environment
assert_not_openai_api_key()

with temporary_openai_api_key():
    response: ChatCompletion = openai_chat()
    # rprint(response)

'''
# Log the request options
logging.debug("Request options: %s", {
    'method': 'post',
    'url': '/chat/completions',
    'files': None,
    'json_data': {
        'messages': [{'role': 'user', 'content': "Hey! Was geht ab?"}],
        'model': 'gpt-3.5-turbo'
    }
})'''

# Sending HTTP Request: POST https://api.openai.com/v1/chat/completions
