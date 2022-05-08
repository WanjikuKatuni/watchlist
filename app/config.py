class Config:
    ''' 
    general config of parent class
    '''
    pass

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