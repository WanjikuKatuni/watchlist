#folder where requests to API will be made
##from app import app #Import app instance
import urllib.request,json # helps create connection to API url and send request to json which formats json response to python dictionary.
from .models import Movie




#Movie=movie.Movie


#getting api key
##api_key = app.config['MOVIE_API_KEY'] #get api key from config object

#getting movie base url
##base_url = app.config["MOVIE_API_BASE_URL"] #acces cibfuguartion objects through api.config and access the movie url


#getting api key
api_key=None

#gtting movie base url
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['MOVIE_API_KEY'] #get api key from config object
    base_url = app.config['MOVIE_API_BASE_URL'] #acces cibfuguartion objects through api.config and access the movie url



def get_movies(category):

    get_movies_url=base_url.format(category,api_key) #replace category and apikey in curly braces of base url
    '''get movies url becomes the final url in the api request '''

    #use with as a contex tmanageer that sendds a request using the urlopen() function abd ass tthe movies data variab;e
    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data=url.read() # read the url and store it in getmoviesdata variable
        get_movies_response = json.loads(get_movies_data) #convert the json response to a pyhtondisctionary using json.losds function and pasing the getmoviesdata variable

        movie_results = None

        if get_movies_response['results']: #resutls from json
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list) #process results takes in list of dictionary obejects and returns list of movie objects
            #movie results gives list of movie objects
    return movie_results

def process_results(movie_list): #pfunction process resutls that takes in list of dictionaries
    '''
    proceses the movie result and transform them to a list of objects

    args:
        movie_list:a list of dictionaties which contain movie details

    Returns:
        movie_results: a list of movie objects
    '''
    movie_results = [] #empty movie results oobject whihc will store newly created movie objects
    for movie_item in movie_list: #loop through list of dictionaries and use get method to access the values
        id = movie_item.get('id')
        title =  movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster=movie_item.get('poster_path')
        vote_average= movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count) #check if movie item has all the required things in the object
            movie_results.append(movie_object)

    return movie_results

def get_movie(id):
    get_movie_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie.object = None
            
        if movie_details_response:
            id=movie_details_response.get('id')
            title=movie_details_response.get('original_title')
            overview= movie_details_response.get('overview')
            poster=movie_details_response.get('poster_path')
            vote_average=movie_details_response.get('vote_average')
            vote_count=movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
    return movie_object

def search_movie(movie_name):
    search_movie_url= 'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,movie_name)
    '''
    the url search request that passes in the api_key and movie_name
    '''

    with urllib.request.urlopen(search_movie_url) as url:
        search_movie_data = url.read()
        search_movie_response = json.loads(search_movie_data)

        search_movie_results = None

        if search_movie_response['results']:
            search_movie_list = search_movie_response['results']
            search_movie_results = process_results(search_movie_list)

    return search_movie_results

