class Config:
    TESTING = False
    DEBUG = False
    LOG_LEVEL = "INFO"
    BASE_URL = "https://api.spacexdata.com"

    @staticmethod
    def __init__(self):
        pass


class TestingConfig(Config):
    TESTING = True
    DEBUG = False


class DevConfig(Config):
    DEBUG = True


config = {
    "Testing": TestingConfig,
    "Default": DevConfig,
    "Development": DevConfig,
}
