from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import re
import os

def clean_text(text):
    return re.sub(r'[^a-zA-Z0-9,.\\"\']', '', str(text))

clean_text_udf = udf(clean_text, StringType())

spark = SparkSession.builder \
    .appName("BronzeToSilver") \
    .getOrCreate()

tables = ["athlete_bio", "athlete_event_results"]
input_dir = "batch_pipeline/output/bronze"
output_dir = "batch_pipeline/output/silver"
os.makedirs(output_dir, exist_ok=True)

for table in tables:
    print(f"📥 Reading bronze table: {table}")
    df = spark.read.parquet(f"{input_dir}/{table}")

    for col_name, dtype in df.dtypes:
        if dtype == "string":
            df = df.withColumn(col_name, clean_text_udf(col(col_name)))

    df = df.dropDuplicates()

    print(f"💾 Writing silver table: {table}")
    df.write.mode("overwrite").parquet(f"{output_dir}/{table}")

    print(f"✅ Done: {table}")

spark.stop()
