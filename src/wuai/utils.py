from contextlib import contextmanager
from typing import Any, Callable
import openai
import os
from dotenv import load_dotenv

def requires_dotenv(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        load_dotenv()
        return func(*args, **kwargs)
    return wrapper

@requires_dotenv
@contextmanager
def temporary_openai_api_key(new_key: str | None = None):
    original_api_key: str | None = openai.api_key
    openai.api_key = new_key or os.getenv("TEST_OPENAI_API_KEY")#from dotenv
    try:
        yield
    finally:
        openai.api_key = original_api_key

def assert_not_openai_api_key():
    load_dotenv()
    if "OPENAI_API_KEY" in os.environ:
        raise ValueError("OPENAI_API_KEY should not be defined in the environment variables.")
