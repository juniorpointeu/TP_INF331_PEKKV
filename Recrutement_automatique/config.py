import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://jordan193:0123456789@localhost/candidats'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
