import csv
import json
from time import sleep
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

with open("data/athlete_event_results.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        producer.send("athlete_events", row)
        print(f"Sent message: {row}")
        sleep(0.1) 
