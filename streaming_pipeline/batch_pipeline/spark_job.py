from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder \
        .appName("Athlete Events ETL") \
        .getOrCreate()

    df = spark.read.csv("batch_pipeline/data/athlete_events.csv", header=True, inferSchema=True)

    df_cleaned = df.dropna(subset=["Name", "Sex", "Age", "Team"])  

    df_cleaned.write.mode("overwrite").parquet("batch_pipeline/output/athlete_events_cleaned")

    spark.stop()

if __name__ == "__main__":
    main()
