# 🌀 Kafka Streaming Pipeline — Final Project (Part 1)

This is the first part of the final Data Engineering project. It demonstrates how to build and verify a **real-time streaming pipeline** using:

- 🐍 Python (`producer.py` script)
- 🐘 Apache Kafka (inside Docker containers)
- 🐳 Docker Compose
- 🔌 Kafka topic: `athlete_events`
- 👀 `kcat` tool to verify that messages are successfully received by Kafka

---

## ✅ What Implemented

1. **Configured Apache Kafka + Zookeeper using Docker Compose**
2. **Created a Kafka topic `athlete_events`**
3. **Developed a Python producer script** that reads events from a CSV file and sends them to Kafka
4. **Used `kcat` (formerly kafkacat)** to consume and validate that messages arrive correctly
5. **Resolved library conflict (`six.py`) in `kafka-python`** to enable message sending
6. **Verified each step with terminal output and screenshots**

---

## 🖼️ Screenshots

| Step | Description                            | Screenshot                                |
| ---- | -------------------------------------- | ----------------------------------------- |
| 1    | ✅ Kafka and Zookeeper running         | ![](screenshots/01_docker_ps.png)         |
| 2    | ✅ Topic `athlete_events` exists       | ![](screenshots/02_kafka_topics_list.png) |
| 3    | ✅ Python producer is sending messages | ![](screenshots/03_producer_running.png)  |
| 4    | ✅ JSON messages received in `kcat`    | ![](screenshots/04_kcat_messages.png)     |

---

## 🚀 How to Run It

### 🐳 Step 1: Start Kafka & Zookeeper

```bash
docker-compose up -d
```

Check running containers:

```bash
docker ps
```

📸 Screenshot: `screenshots/01_docker_ps.png`

---

### 📑 Step 2: Verify Kafka Topic

```bash
docker exec -it streaming_pipeline-kafka-1   kafka-topics --bootstrap-server localhost:9092 --list
```

📸 Screenshot: `screenshots/02_kafka_topics_list.png`

---

### 🐍 Step 3: Run Python Producer (in Ubuntu/WSL)

```bash
python producer.py
```

📸 Screenshot: `screenshots/03_producer_running.png`

---

### 🔍 Step 4: Run Kafka Consumer (PowerShell)

```bash
docker run --rm -it --network streaming_pipeline_default edenhill/kcat:1.7.0 \
  kcat -b streaming_pipeline-kafka-1:9092 -t athlete_events -C
```

📸 Screenshot: `screenshots/04_kcat_messages.png`

---

## 🛠️ Troubleshooting Notes

- ❗ Fix `six.py` issue in kafka-python:

```bash
cp .venv/lib/python3.12/site-packages/six.py \
   .venv/lib/python3.12/site-packages/kafka/vendor/six.py
```

- ❗ If topic or containers don't work:

```bash
docker-compose down
docker-compose up -d
```

---
