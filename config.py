import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Connecting to the database

SQLALCHEMY_DATABASE_URI = 'postgresql://odunayoakinlade@localhost:5432/fyyur'
