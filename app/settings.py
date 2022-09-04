import pydantic


class Settings(pydantic.BaseSettings):
    MONGO_URI: pydantic.AnyUrl = "mongodb://localhost:27017/morotech"

    class Config:
        env_file = ".env"


settings = Settings()
