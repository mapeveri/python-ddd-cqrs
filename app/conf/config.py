import os

# Grabs the folder where the script runs.
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Secret key for initialize management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = os.getenv('APP_SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Debug mode
DEBUG = os.getenv("FLASK_DEBUG")

# Celery
broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = 'rpc://'
result_persistent = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_CONNECTION")

ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')