from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, current_timestamp

spark = SparkSession.builder \
    .appName("SilverToGold") \
    .getOrCreate()

base_path = "/mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline"

bio_df = spark.read.parquet(f"{base_path}/batch_pipeline/output/silver/athlete_bio") \
    .withColumnRenamed("country_noc", "bio_country_noc")

events_df = spark.read.parquet(f"{base_path}/batch_pipeline/output/silver/athlete_event_results")

df = events_df.join(
    bio_df.select("athlete_id", "sex", "bio_country_noc"), on="athlete_id", how="inner"
)

agg_df = df.groupBy("sport", "medal", "sex", "bio_country_noc") \
    .agg(
        avg(col("weight").cast("float")).alias("avg_weight"),
        avg(col("height").cast("float")).alias("avg_height")
    )

agg_df = agg_df.withColumn("timestamp", current_timestamp())

agg_df.write.mode("overwrite").parquet(f"{base_path}/batch_pipeline/output/gold/avg_stats")

print("✅ Gold dataset successfully created.")

spark.stop()
