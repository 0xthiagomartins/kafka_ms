from nameko_kafka import KafkaProducer, KafkaConsumer
from nameko.rpc import rpc
from .config import config


class MicroServiceA:
    name = config["SERVICE_NAME"]

    kafka_producer = KafkaProducer()
    kafka_consumer = KafkaConsumer(topics=[config["TOPIC_NAME"]])

    @rpc
    def method_A(self, param1):
        # Produce a message to Kafka
        self.kafka_producer.produce(
            topic=config["TOPIC_NAME"], value=f"Message: {param1}"
        )

        # Example Kafka consumer usage
        consumed_messages = []
        for message in self.kafka_consumer:
            consumed_messages.append(message.value.decode("utf-8"))
            break  # For demonstration purposes, we just consume one message

        return f"Produced message: {param1}, Consumed messages: {consumed_messages}"
