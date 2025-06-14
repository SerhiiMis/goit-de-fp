from pyspark.sql import SparkSession
import os

spark = SparkSession.builder \
    .appName("LandingToBronze") \
    .getOrCreate()

tables = {
    "athlete_bio": "/mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/data/athlete_bio.csv",
    "athlete_event_results": "/mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/data/athlete_event_results.csv"
}

bronze_dir = "/mnt/d/Projects/repositories/goit-de-fp/streaming_pipeline/batch_pipeline/output/bronze"
os.makedirs(bronze_dir, exist_ok=True)

for name, path in tables.items():
    print(f"📥 Reading {name} from {path}")
    df = spark.read.option("header", "true").csv(path)

    print(f"💾 Writing {name} to {bronze_dir}/{name}")
    df.write.mode("overwrite").parquet(f"{bronze_dir}/{name}")

    print(f"✅ Done: {name}")

spark.stop()
