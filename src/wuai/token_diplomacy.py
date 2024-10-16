# from get_access_token import get_access_token,
import time, os

import requests
from requests.auth import HTTPBasicAuth
from wuai.logging_config import setup_logging
from wuai.settings import Settings, Payload
from wuai.status_code_exception import StatusCodeException, Timeout, TimeoutException
from wuai.post2api import post_data, get_access_token

from pprint import pprint
from rich import print as rprint


class TokenDiplomat(Settings):
    # def __post_init__(self):
    #     super().__post_init__()
    #     self.refresh_token()

    @property
    def token(self):
        if not hasattr(self, "_response"):
            self.refresh_token()
        if self.remaining_time() <= 0:  # equality on __init__
            self.refresh_token()
        return self._response["access_token"]

    @property
    def merit(self):
        """json of requests.post for token"""
        token_merit = {
            "url": self.token_url,
            "auth": HTTPBasicAuth(username=self.client_id, password=self.client_secret),
            "data": self.payload.model_dump(),
            # data={
            #'grant_type': 'CLIENT_CREDENTIALS',        # cursor: ignore
            #'scope': Url('api://bbeee3.../.default')}  # cursor: ignore
            "timeout": 10,
        }
        self._merit = token_merit  # noqa
        return self._merit

    def remaining_time(self):
        """int (s) of time remaining on token"""
        if not hasattr(self, "_t0"):
            self.refresh_token()
        return self._response["expires_in"] - int((time.time() - self._t0))

    def refresh_token(self, timeout_requests: int = 10):
        try:
            with Timeout(timeout_requests):
                response = requests.post(**self.merit)
                response.raise_for_status()
                self._t0 = time.time()
                self._response = response.json()  # noqa
                return self._response["access_token"]
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to request token: {e}")
        except TimeoutException as e:
            raise RuntimeError(f"Request timed out: {e}")
        except StatusCodeException as e:
            raise RuntimeError(f"Status code exception: {e}")


def debug_setup():
    from wuai.token_diplomacy import TokenDiplomat, Settings

    td = TokenDiplomat()
    token = td.token  # AZURE_OPENAI_AD_TOKEN
    merit = td.merit
    settings = Settings()

    rprint(f"{settings=}")
    rprint(f"{td.payload=}")

    rprint(f"POST for token:\n,{td.merit=}")
    rprint(f"token:\n{td.token[:20]=}")

    messages = {
        "messages": [{"role": "user", "content": "Was ist der erste Buchstabe des Alphabets?"}]
    }
    headers: dict[str, str] = {
        "Authorization": f"Bearer {td.token}",
        "Content-Type": "application/json",
    }

    post_data_options = dict(url=td.api.gpt4o, json=messages, headers=headers)
    rprint(f"POST options for completion:\n", post_data_options)

    result = post_data(api_url=td.api.gpt4o, token=td.token, data=messages)  # noqa
    message_content = result["choices"][0]["message"]["content"]
    rprint(f"POST for completion:\n{message_content}")

    return result, td, settings


if __name__ == "__main__":
    setup_logging()
    # Enable HTTP debugging
    import http.client as httplib

    httplib.HTTPConnection.debuglevel = 1

    result, td, settings = debug_setup()

    """ #TODO: Refactor
    messages = {
        "messages": [{"role": "user", "content": "Was ist der erste Buchstabe des Alphabets?"}]
    }
    headers: dict[str, str] = {"Authorization": f"Bearer {td.token}", "Content-Type": "application/json"}
    post_data_options = dict(url=td.api.gpt4o, json=messages, headers=headers)
    """

    """
        # result_requests = requests.post(**post_data_options)
        # message_content_requests = result_requests.json()['choices'][0]['message']['content']
        # rprint(f"POST for completion:\n{message_content_requests}")

        # these two are equivalent (10/16/2024)

        # result_post2api = post_data(api_url=ts.api.gpt4o, token=ts.token, data=messages)  # noqa
        # message_content_post2api = result_post2api["choices"][0]["message"]["content"]
        # rprint(f"POST for completion:\n{message_content_post2api}")
    """

    # #httplib debug result
    #     send: b'POST /base-gpt-4o-128k/v1/chat/completions HTTP/1.1\r\n'\
    #           b'Host: api.openai.wustl.edu\r\n'\
    #           b'User-Agent: python-requests/2.32.3\r\n'\
    #           b'Accept-Encoding: gzip, deflate\r\n'\
    #           b'Accept: */*\r\n'\
    #           b'Connection: keep-alive\r\n'\
    #           b'Authorization: Bearer eyJ...RZQ\r\n'\
    #           b'Content-Type: application/json\r\n'\
    #           b'Content-Length: 89\r\n'\
    #           b'\r\n'

    """ ## -- ## It should look like this: ## -- ## #! 
    POST for completion:
        {'url': Url('https://api.openai.wustl.edu/base-gpt-4o-128k/v1/chat/completions'), 
        'json': {'messages': [
            {'role': 'user', 
            'content': 'Was ist der erste Buchstabe des Alphabets?'}]},
        'headers': {
            'Authorization': 'Bearer eyJ0eXAiOi...SeUNkNg', 
            'Content-Type': 'application/json'}
        }
    """
