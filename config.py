import os


basedir = os.path.abspath(os.path.dirname(__file__))
 
 
class Config(object):
    DEBUG = False
    TESTING = False
 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}
 
    SITE_NAME = ''
 
    THREADS_PER_PAGE = 2
 
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
 
 
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'APP_PRODUCTION_DATABASE_URI'
    )
 
 
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + basedir + '/sqlite.db'
    
    
class TestingConfig(Config):
     TESTING = True
     SQLALCHEMY_DATABASE_URI = os.environ.get(
         'APP_TESTING_DATABASE_URI'
     )
 
 
 config = {
     'production': ProductionConfig,
     'development': DevelopmentConfig,
     'testing': TestingConfig,
     'default': DevelopmentConfig,
 }
