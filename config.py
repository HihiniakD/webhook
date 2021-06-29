import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql:///webhook'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REQUESTS_PER_PAGE = 50


