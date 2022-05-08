from flask import Flask 
from .config import DevConfig

#init app
app= Flask(__name__,instance_relative_config = True) #instance_relative allows us to connect to instance. folder

#set up config
app.config.from_object(DevConfig) #Setup configuration and pass the devconfig subclass
app.config.from_pyfile('config.py') #connects to config file in app folder and appened by app.config

from app import views #this allows us to create views