import os


class BaseConfig:
    DEBUG = False
    TESTING = False

    MONGO_URI = os.getenv(
        "MONGO_URI",
        "mongodb://localhost:27017/logdb"
    )


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/logdb_test"


class ProductionConfig(BaseConfig):
    MONGO_URI = os.getenv("MONGO_URI")