import os

# Grabs the folder where the script runs.
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# Secret key for initialize management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = os.getenv('APP_SECRET_KEY')

SQLALCHEMY_TRACK_MODIFICATIONS = False

# Debug mode
DEBUG = bool(os.getenv("FLASK_DEBUG"))

# Celery
broker_url = os.getenv('CELERY_BROKER_URL')
result_backend = 'rpc://'
result_persistent = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_CONNECTION")

ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')

ALLOWED_CLIENT_URL = os.getenv('ALLOWED_CLIENT_URL')
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')

# Email
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
MAIL_SENDER = os.getenv('MAIL_SENDER')
MAIL_RECIPIENT = os.getenv('MAIL_RECIPIENT')
