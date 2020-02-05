from kafka import KafkaConsumer
from utils import TOPIC


def consume():
    consumer = KafkaConsumer(TOPIC, auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'],
                             api_version=(0, 10), consumer_timeout_ms=3000)  # TODO: remove the hardcoded values
    try:
        for msg in consumer:
            print(msg.key.decode('utf-8'), int(msg.value), sep=": ")
    except KeyboardInterrupt:
        print("Interrupted!")

    if consumer is not None:
        consumer.close()


if __name__ == "__main__":
    consume()
