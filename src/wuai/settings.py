import os
from rich import print as rprint

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, BaseModel, HttpUrl, AnyUrl

wustl_api_settings = SettingsConfigDict(
    env_prefix="WUSTL_API_", env_nested_delimiter="__"
)

class Payload(BaseModel):
    grant_type: str
    scope: AnyUrl

class API(BaseSettings):
    model_config = wustl_api_settings
    gpt4: HttpUrl 
    gpt4o: HttpUrl

class Settings(BaseSettings):
    model_config = wustl_api_settings
    token_url: HttpUrl = Field(serialization_alias="url")
    client_id: str
    client_secret: str
    scope: str
    gpt4 : HttpUrl  
    gpt4o: HttpUrl

    payload: Payload
    
    api: API = API()


if __name__ == "__main__":
    settings = Settings()
    rprint(settings)





