import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_CONFIG = {
    "url": "jdbc:mysql://217.61.57.46:3306/olympic_dataset",
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "driver": "com.mysql.cj.jdbc.Driver",
}
