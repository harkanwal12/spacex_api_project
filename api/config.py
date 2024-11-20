class Config:
    LOG_LEVEL = "INFO"
    BASE_URL = "https://api.spacexdata.com"


class TestingConfig(Config):
    TESTING = True
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    TESTING = False


class ProdConfig(Config):
    TESTING = False
    DEBUG = False


config = {
    "Testing": TestingConfig,
    "Default": DevConfig,
    "Development": DevConfig,
    "Production": ProdConfig,
}
