from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, current_timestamp

spark = SparkSession.builder \
    .appName("SilverToGold") \
    .getOrCreate()

bio_df = spark.read.parquet("batch_pipeline/output/silver/athlete_bio") \
    .withColumnRenamed("country_noc", "bio_country_noc")

bio_df_selected = bio_df.select("athlete_id", "sex", "bio_country_noc", "height", "weight")

events_df = spark.read.parquet("batch_pipeline/output/silver/athlete_event_results")

df = events_df.join(bio_df_selected, on="athlete_id", how="inner")

agg_df = df.groupBy("sport", "medal", "sex", "bio_country_noc") \
    .agg(
        avg(col("weight").cast("float")).alias("avg_weight"),
        avg(col("height").cast("float")).alias("avg_height")
    )

agg_df = agg_df.withColumn("timestamp", current_timestamp())

agg_df.show()

agg_df.write.mode("overwrite").parquet("batch_pipeline/output/gold/avg_stats")

print("✅ Gold dataset successfully created.")

spark.stop()
