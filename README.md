# food-delivery-backend-kafka
Built a Kafka-based messaging system using Python producers and consumers, Dockerized Kafka (KRaft mode), and local development setup to understand distributed messaging systems.

## Tech Stack
- Python
- Apache Kafka (Confluent cp-kafka)
- Docker + Docker Compose

## Features
- Kafka Producer publishes food order events
- Kafka Consumer/tracker reads and processes events

## Setup

### 1. Start Kafka
bash
docker compose -f docker-compose.yaml up -d

### 2. Activate virtual environment

source .venv/bin/activate

pip install confluent-kafka

### 3. Run Producer
python producer.py

### 4. Run Consumer
python tracker.py

### Notes

Kafka is running in KRaft mode (no Zookeeper).
