import os #alllow aplication to interact with the OS

class Config:
    ''' 
    general config of parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}' #{} This are sections which will be replaced with actual values
    pass
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get(SECRET_KEY)

class ProdConfig(Config):
    '''
    production configuration child class
    Args:
    config:the parent configuttion class with general configutation settings
    '''
    pass
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
    config: parent config with generla config settings
    '''
    pass

    DEBUG = True
#createdictionary to help in configuration of option classes
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}