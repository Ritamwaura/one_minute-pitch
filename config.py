import os


class config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Rita:123@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
    
    
    class Prodconfig(config):
        SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://Rita:123@localhost/pitch'
        
        
        DEBUG = True
        
        
        
    class TestConfig(Config):
        pass
        # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Rita:123@localhost/pitch_test'
        # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    class DevConfig(Config):
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Rita:123@localhost/pitch'
        # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        DEBUG = True
    

