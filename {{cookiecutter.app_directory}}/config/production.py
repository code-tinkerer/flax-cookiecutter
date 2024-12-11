import os

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

if SECRET_KEY is None:
    raise ValueError("Please set the environment variable 'SECRET_KEY'")

ENV = "production"

DEBUG = False
DEVELOPMENT = False
TESTING = False
