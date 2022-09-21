import os

# Grabs the folder where the script runs.
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Secret key for initialize management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = 'my-secret-key'

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable debug mode.
DEBUG = True

CELERY_BROKER_URL = 'amqp://app:rabbit_app@rabbitmq:5672',
RESULT_BACKEND = 'rpc://'

# Connect to the database
POSTGRESQL = 'postgresql+psycopg2://postgres:app123456@db/marketplace'
SQLALCHEMY_DATABASE_URI = POSTGRESQL

ELASTICSEARCH_URL = 'http://elasticsearch:9200'
