from flask import Flask 
from .config import DevConfig

#init app
app= Flask(__name__)

#set up config
app.config.from_object(DevConfig) #Setup configuration and pass the devconfig subclass

from app import views #this allows us to create views