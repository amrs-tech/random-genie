# keep this file and other files used by the create_app function free of inner-project import statements to help
# prevent circular imports.  Setting up cache in a separate cache.py file similar to this config.py file is very helpful.
import os

class Config:
    # user configurations
    flask_debug = False

    # flask configurations
    SECRET_KEY = 'askjdfkajsdfksdf'

    # DB config
    DB_HOST = os.environ.get("DB_HOST","localhost")
    DB_NAME = os.environ.get("DB_NAME","viz_app")
    DB_USER = os.environ.get("DB_USER","root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD","Livemocha.123")
