from flask import render_template #takes name of the template file index.html as first argument and searchs it in the app/template subdirectory
from app import app #impot app instance from the app folder


#views
@app.route('/')
def index():

    ''' 
    view root page function which returns the index page and the data it has 
    '''
    return render_template('index.html')