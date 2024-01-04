import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True

#db_user = os.environ['DB_USER']
#db_password = os.environ['DB_PASSWORD']
#db_name = os.environ['DB_NAME']
#db_host = os.environ['DB_HOST']
SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")             
SQLALCHEMY_TRACK_MODIFICATIONS = False