from flask import Blueprint

trans = Blueprint('trans', __name__)

from . import views
