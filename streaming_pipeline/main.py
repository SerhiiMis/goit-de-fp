from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ReadAthleteBioCSV") \
    .getOrCreate()

bio_df = spark.read.csv("data/athlete_bio.csv", header=True, inferSchema=True)

clean_bio_df = bio_df.filter(
    col("height").cast("float").isNotNull() &
    col("weight").cast("float").isNotNull()
)

clean_bio_df.show(10)

