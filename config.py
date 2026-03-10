import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    USERNAME = os.getenv('USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    LOCKED_USER = os.getenv('LOCKED_USER')
    
    FIRST_NAME = os.getenv('FIRST_NAME')
    LAST_NAME = os.getenv('LAST_NAME')
    POSTAL_CODE = os.getenv('POSTAL_CODE')