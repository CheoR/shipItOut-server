from .base import *

DEBUG = False
# update deploy-this-test to your app name
ALLOWED_HOSTS = ['deploy-this-test.herokuapp.com']

CORS_ORIGIN_WHITELIST = (
    'https://deploy-this-test.herokuapp.com',
)
