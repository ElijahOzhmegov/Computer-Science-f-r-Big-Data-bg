from kafka_utils import connect_kafka_consumer


def read_messages(_consumer):
    try:
        for msg in _consumer:
            print(msg.key.decode('utf-8'), int(msg.value), sep=": ")
    except KeyboardInterrupt:
        print("Interrupted!")


def consume():
    consumer = connect_kafka_consumer()
    read_messages(consumer)
    if consumer is not None: consumer.close()

if __name__ == "__main__":
    consume()
