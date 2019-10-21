from flask import Blueprint
main = Blueprint('main',__name__)
from . import views,error
from flask_uploads import UploadSet,configure_uploads,IMAGES


photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    # configure UploadSet
    configure_uploads(app,photos)
