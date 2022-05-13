from flask import Blueprint #import blueprint from flask
main = Blueprint('main', __name__)  #initialise the blueprint class by creatign variable main  whcih is the name of the blueprint and the na,e variable which finds the location of the blueprint
from . import views, error #to avoid circular dependencies

