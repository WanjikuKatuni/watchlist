from flask import render_template #takes name of the template file index.html as first argument and searchs it in the app/template subdirectory
from app import app #impot app instance from the app folder


#views
@app.route('/')
def index():

    ''' 
    view root page function which returns the index page and the data it has 
    '''
    title='Home - Welcome to The best Movie Review Website Online'
    
    return render_template('index.html', title=title)  #first messgae is the variable in the  template, the second message is variablein the view function

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    title = 'Movie {{ic}}'
    return render_template('movie.html', id=movie_id)