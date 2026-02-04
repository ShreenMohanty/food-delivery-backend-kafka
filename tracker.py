from confluent_kafka import Consumer
import json

consumer = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'order-tracker-id', 'auto.offset.reset': 'earliest'})

consumer.subscribe(['order'])
print("Consumer is running and subscribed to order topic")

try:
    while True:
        msg = consumer.poll(1.0)      #consumers poll asking kafka for new events/messages instead of kafka stacking everything into them. As a consumer can subscibe to multiple topics, they get to decide how and when they want datat
        if msg is None:
            continue
        if msg.error():
            print("Error", msg.error())
            continue
        value = msg.value().decode('utf-8')
        order = json.loads(value)

        print(f"received order {order}")
        print(f"received qty: {order['quantity']} x {order['item']} from {order['user']}")

except KeyboardInterrupt:
    print("Stopping consumer")

finally:   #in case some other error happens still we ALWAYS want to close the consumer gracefully rightt
    consumer.close()
