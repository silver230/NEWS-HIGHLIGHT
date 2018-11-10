from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

def create_app(config_name):
    
    # app = Flask(__name__)
    app = Flask(__name__,instance_relative_config = True)
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # setting config
    from .requests import configure_request
    configure_request(app)


    return app