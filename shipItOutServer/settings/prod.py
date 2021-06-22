from .base import *

DEBUG = False
# update deploy-this-test to your app name
ALLOWED_HOSTS = ['shipitout-api.herokuapp.com',
                 'shipitout.herokuapp.com']

CORS_ORIGIN_WHITELIST = (
    'https://shipitout-api.herokuapp.com',
    'https://shipitout.herokuapp.com'
)
