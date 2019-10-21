rom flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PitchForm
from ..models import Review,User,Pitch
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  