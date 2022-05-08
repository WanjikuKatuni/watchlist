from flask import Flask 

#init app
app= Flask(__name__)

from app import views #this allows us to create views