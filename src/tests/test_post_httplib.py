"""test_post_httplib.py

delete me eventually.

"""

from wuai.token_diplomacy import rprint,pprint, os

import openai

from tests.test_post import temporary_openai_api_key, openai_chat
# from tests.test_post import http_client_logger


## Works amazing!!vz
#   # or maybe it didnt' do anything
# Enable HTTP debugging
import http.client as httplib
httplib.HTTPConnection.debuglevel = 1

with temporary_openai_api_key():
    response = openai_chat()
    rprint(response)




