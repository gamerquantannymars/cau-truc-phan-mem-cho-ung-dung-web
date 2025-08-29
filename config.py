import os

class Config:
    # Database URI configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'sqlite:///site.db'
    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
