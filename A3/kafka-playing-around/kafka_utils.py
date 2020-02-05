import kafka

SPACE = ['localhost:9092']
API_VERSION = (0, 10)
ENCODING = 'utf-8'
TOPIC = "numbers"


def connect_kafka_producer():
    _producer = None
    try:
        _producer = kafka.KafkaProducer(bootstrap_servers=SPACE, api_version=API_VERSION)
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


def connect_kafka_consumer():
    _consumer = None
    try:
        _consumer = kafka.KafkaConsumer(TOPIC, auto_offset_reset='earliest',
                                        bootstrap_servers=SPACE,
                                        api_version=API_VERSION,
                                        consumer_timeout_ms=3000)  # TODO: remove the hardcoded value
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _consumer


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes   = bytes(key,   encoding=ENCODING)
        value_bytes = bytes(value, encoding=ENCODING)
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))

