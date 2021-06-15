import os

class Config(object):
    DEBUG = False
    TESTING = False
    MYSQL_HOST = os.environ['MYSQL_HOST']
    MYSQL_USER = os.environ['MYSQL_USER']
    MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']
    MYSQL_DB = os.environ['MYSQL_DB']
    MYSQL_PORT = 3306
    DEFAULT_MAIL_SENDER = os.environ['DEFAULT_MAIL_SENDER']
    SECURITY_PASSWORD_SALT = os.environ['SECURITY_PASSWORD_SALT']
    SECRET_KEY = os.environ['SECRET_KEY']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ['MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
    STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']