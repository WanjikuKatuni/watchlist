#folder where requests to API will be made
from app import app #Import app instance
import urllib.request,json # helps create connection to API url and send request to json which formats json response to python dictionary.
from.models import movie

Movie=movie.Movie

#getting api key
api_key=app.config['MOVIE_API_KEY'] #get api key from config object

#getting movie base url
base_url = app.config["MOVIE_API_BASE_URL"] #acces cibfuguartion objects through api.config and access the movie url

