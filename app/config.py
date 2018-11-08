class Config:
    '''
    General configuration parent class
    '''
    
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    SOURCES_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    NEWS_API_KEY = 'f4bcda214f414713a966961fdae13472'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True    

