from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
#from .config import DevConfig

#init app
#app= Flask(__name__,instance_relative_config = True) #instance_relative allows us to connect to instance. folder

#set up config
#app.config.from_object(DevConfig) #Setup configuration and pass the devconfig subclass
#app.config.from_pyfile('config.py') #connects to config file in app folder and appened by app.config

#intializing flask extensions
bootstrap = Bootstrap() #pass in the app instance

def create_app(config_name):

    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #registering the blueprint inside the application factory
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from.request import configure_request
    configure_request(app)

    return app



#from app import views #this allows us to create views
#from app import error #this allow us to create error