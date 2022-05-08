#folder where requests to API will be made
from app import app #Import app instance


#getting api key
api_key=app.config['MOVIE_API_KEY'] #get api key from config object