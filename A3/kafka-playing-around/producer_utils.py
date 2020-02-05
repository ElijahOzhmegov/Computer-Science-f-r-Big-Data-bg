import time
from kafka_utils import publish_message, connect_kafka_producer, TOPIC


def infinite_sequence(even=True):
    num = 0 if even else 1
    while True:
        yield num
        num += 2


def produce_numbers(kafka_producer_, sleep_time=2, even=True):
    try:
        key = 'Producer A' if even else 'Producer B'
        for number in infinite_sequence(even):
            publish_message(kafka_producer_, TOPIC, key, str(number))
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("Interrupted!")


def produce(sleep_time, even):
    kafka_producer = connect_kafka_producer()
    produce_numbers(kafka_producer, sleep_time, even)

    if kafka_producer is not None:
        kafka_producer.close()


if __name__ == '__main__':
    def test_infinite_sequence(even):
        i = 0 if even else 1
        for item in infinite_sequence(even):
            assert item == i
            i += 2
            if i > 20: break

    test_infinite_sequence(even=True)   # even numbers
    test_infinite_sequence(even=False)  # odd  numbers

