from flask import render_template #takes name of the template file index.html as first argument and searchs it in the app/template subdirectory
from app import app #impot app instance from the app folder
from .request import get_movies # import getmovies 

#views
@app.route('/')
def index():

    ''' 
    view root page function which returns the index page and the data it has 
    '''
    #popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    
    title='Home - Welcome to The best Movie Review Website Online'
    
    return render_template('index.html', title = title, popular = popular_movies, upcoming=upcoming_movies, now_playing=now_showing_movies)  #first messgae is the variable in the  template, the second message is variablein the view function

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = 'Movie {{id}}'
    return render_template('movie.html', id=movie_id)