from os import getenv


SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://app:password@localhost/hw_dc",
)


class Config(object):
    DEBUG = False
    TESTING = False
    ENV = "development"
    SECRET_KEY = 'gjsu-hgjfzvnzcxjigfh-vnxlz'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    ENV = "production"
    SECRET_KEY = "kj;io;lkmkjciojndcl/zlkmc/"


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
