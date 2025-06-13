from pyspark.sql import SparkSession
from config import MYSQL_CONFIG

spark = SparkSession.builder \
    .appName("ReadAthleteBio") \
    .config("spark.jars", "mysql-connector-j-8.0.32.jar") \
    .getOrCreate()

df = spark.read.format("jdbc").options(
    url=MYSQL_CONFIG["url"],
    driver=MYSQL_CONFIG["driver"],
    dbtable="athlete_bio",
    user=MYSQL_CONFIG["user"],
    password=MYSQL_CONFIG["password"]
).load()

df.show(5)
