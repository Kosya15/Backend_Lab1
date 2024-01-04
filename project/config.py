import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True

db_user = os.environ.get('DB_USER', 'post')
db_password = os.environ.get('DB_PASSWORD', 'son1540')
db_name = os.environ.get('DB_NAME', 'lab3DB')
db_host = os.environ.get('DB_HOST', 'localhost')

SQLALCHEMY_DATABASE_URI = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"
SQLALCHEMY_TRACK_MODIFICATIONS = False