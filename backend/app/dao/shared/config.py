from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
database = os.getenv('DB_NAME')

DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"