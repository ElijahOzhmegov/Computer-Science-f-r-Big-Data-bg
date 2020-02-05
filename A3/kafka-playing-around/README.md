# A3 Streaming / Messaging with Apache Kafka

## 0. My notes

Apache Kafka is an open-source stream processing software platform. 
It easily handles real-time data feeds and can be used for the 
following purposes:
1. Activity Monitoring 
2. Messaging
3. Log Aggregation
4. ETL (Extraction, Transformation, Loading) **Hello from BI**
5. Database

To launch **Apache-Kafka** it essential to launch **Apache-Zookeeper**,
because **AK** needs to elect a new controller (sometimes),
watch over cluster members (always), to configure a topic and a few
another important actions, which can be found [here](https://www.quora.com/What-is-the-actual-role-of-Zookeeper-in-Kafka-What-benefits-will-I-miss-out-on-if-I-don%E2%80%99t-use-Zookeeper-and-Kafka-together/answer/Gwen-Shapira).

As I mainly use OSX, I found [this article](https://medium.com/@Ankitthakur/apache-kafka-installation-on-mac-using-homebrew-a367cdefd273)
 also useful, besides 
[provided one](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05).

### Let me also highlight some useful commands for OSX
For linux based OS the main difference is the paths of properties files.
1. To launch a zookeeper server
    ```shell script
    $ zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties
    ```
2. To launch a kafka server
    ```shell script
    $ kafka-server-start /usr/local/etc/kafka/server.properties
    ```
3. To create a kafka topic named as "test"
    ```shell script
    $ kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
    ```
4. To initialize a consumer console (you can easily guess 
what does mean `--from-beginning` option)
    ```shell script
    $ kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning
    ```
5. To initialize a producer console
    ```shell script
    $ kafka-console-producer --broker-list localhost:9092 --topic test
    ```
 
Did you notice it? The different port for the kafka topic. The 
reason for that is Kafka and Zookeeper are different things.
* kafka default port is 9092 (can be changed on `server.properties`);
* zookeeper default port for client connections is 2181.

([source](https://stackoverflow.com/questions/38531054/kafka-and-firewall-rules))

## 1. Kafka Messaging
    Programm (!) two Kafka Producers writing to the same topic (using 
    Java, Python, etc.) Producer A writes even numbers every second,
    the other Producer B writes off numbers every two seconds to the
    topic. Your consumer C reads the numbers and prints them with the 
    origin A or B.
   
There is no doubt that `writes off numbers` is `writes odd numbers`.

Below code for​ **Producer A**​. It writes **even** 
numbers every **second**.
```python
from producer_utils import produce

if __name__ == "__main__":
    produce(sleep_time=1, even=True)
```
Below code for​ **Producer B**​. It writes odd numbers every 
**2 seconds**.
```python
from producer_utils import produce

if __name__ == "__main__":
    produce(sleep_time=2, even=False)
```
Below code for​ **Consumer C**​. It prints values from the topic named 
`numbers`.
```python
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
```
