import os


class config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Rita:123@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'