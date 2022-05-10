from flask import render_template, request, redirect,url_for #takes name of the template file index.html as first argument and searchs it in the app/template subdirectory
from app import app #impot app instance from the app folder
from .request import get_movies, get_movie, search_movie # import getmovies 
from .models import reviews
from .forms import ReviewForm

Review= reviews.Review 

#index template
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
    
    search_movie = request.args.get('movie_query')

    if search_movie:
        return redirect(url_for('search', movie_name=search_movie))
    else:
    
        return render_template('index.html', title = title, popular = popular_movies, upcoming=upcoming_movies, now_playing=now_showing_movies)  #first messgae is the variable in the  template, the second message is variablein the view function

#movie temlplate 
@app.route('/movie/<int:id>')
def movie(id):
    '''
    view movie page function that returns movie details page and its data
    '''
    movie=get_movie(id)
    reviews = Review.get_reviews(movie.id)
    title = f'{movie.title}'
    
    return render_template('movie.html', movie=movie, title=title)

#search view function
@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    view funciton that displays search resutls
    '''

    movie_name_list =movie_name.split(" ") #to return a list of strings seperated by a space
    movie_name_format = "+".join(movie_name_list) #add + sign betwwn the searched words
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}' # fi is used to format the string

    return render_template('search.html', title=title, movies=searched_movies)


@app.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):
    form=ReviewForm()
    movie=get_movie(id)

    if form.validate_on_submit():
        title=form.title.data
        review = form.review.data
        new_review = Review(movie.id, title, movie.poster, review)
        new_review.save_review()
        return redirect(url_for('movie', id=movie.id))
    title = f'(movie.title) review'
    return render_template('new_review.html', title=title, review_form=form, movie=movie)

