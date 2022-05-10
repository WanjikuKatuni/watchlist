from flask import render_template
from app import app

@app.errorhandler(404)
def four_0w_four(error):
    '''
    function to render the 4040 error
    '''

    return render_template('four_0w_four.html'), 404

