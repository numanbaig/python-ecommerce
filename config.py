import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables
SECRET_KEY_VARIABLE = os.getenv('SECRET_KEY')
JWT_SECRET_KEY_VARIABLE = os.getenv('JWT_SECRET_KEY')

class Config:
    SECRET_KEY = SECRET_KEY_VARIABLE
    MONGO_URI = "mongodb://localhost:27017/ecommerce-py"
    JWT_SECRET_KEY = JWT_SECRET_KEY_VARIABLE
