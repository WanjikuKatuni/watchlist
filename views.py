from flask import render_template
from app import app


#views
@app.route('/')
def index():

    ''' 
    view root page function which returns the index page and the data it has 
    '''
    return render_template('index.html')