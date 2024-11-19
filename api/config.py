class Config:
    LOG_LEVEL = "INFO"
    BASE_URL = "https://api.spacexdata.com"


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    CONFIG_TYPE = "TEST"


class DevConfig(Config):
    DEBUG = True
    TESTING = False
    CONFIG_TYPE = "DEV"


class ProdConfig(Config):
    TESTING = False
    DEBUG = False
    CONFIG_TYPE = "PROD"


config = {
    "Testing": TestingConfig,
    "Default": DevConfig,
    "Development": DevConfig,
    "Production": ProdConfig,
}
