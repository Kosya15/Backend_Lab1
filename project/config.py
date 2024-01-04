import os

PROPAGATE_EXCEPTIONS = True
FLASK_DEBUG = True

# db_user = os.environ['DB_USER']
# db_password = os.environ['DB_PASSWORD']
# db_name = os.environ['DB_NAME']
# db_host = os.environ['DB_HOST']
SQLALCHEMY_DATABASE_URI = "postgres://lab3db_o1ps_user:sEXzofH6ojrO5jp3p47KtjIegDedDWTQ@dpg-cmb8hued3nmc73eo9aqg-a/lab3db_o1ps"
SQLALCHEMY_TRACK_MODIFICATIONS = False