from confluent_kafka import Producer
import uuid
import json

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err:
        print(f"Delivery report error: {err}")
    else:
        print(f"Delivery succeeded: {msg.value().decode('utf-8')}")
        print(dir(msg))
        print(f"Delivered to {msg.topic()}: partition {msg.partition()}")

order = {
    "order_id": str(uuid.uuid4()),
    "user": "shreen",
    "item": "chicken biryani",
    "quantity": 3
}

value = json.dumps(order).encode("utf-8")

producer.produce(topic="order", value=value, callback=delivery_report)

producer.flush()