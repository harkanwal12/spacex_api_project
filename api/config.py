class Config:
    LOG_LEVEL = "INFO"
    BASE_URL = "https://api.spacexdata.com"
    FRONTEND_BUILD_DIR = "../client/dist"
    FRONTEND_ROOT_FILE = "index.html"


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    FRONTEND_BUILD_DIR = None
    FRONTEND_ROOT_FILE = None


class DevConfig(Config):
    DEBUG = True
    TESTING = False
    FRONTEND_BUILD_DIR = None
    FRONTEND_ROOT_FILE = None


class ProdConfig(Config):
    TESTING = False
    DEBUG = False


config = {
    "Testing": TestingConfig,
    "Default": DevConfig,
    "Development": DevConfig,
    "Production": ProdConfig,
}
