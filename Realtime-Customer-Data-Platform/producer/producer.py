import json

from kafka import KafkaProducer

from config import (
    KAFKA_BOOTSTRAP_SERVERS,
    KAFKA_TOPIC,
)


class EventProducer:

    def __init__(self):

        self.topic = KAFKA_TOPIC

        self.producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda value: json.dumps(value).encode("utf-8")
        )

    def send(self, event):

        self.producer.send(
            self.topic,
            event.to_dict()
        )

        self.producer.flush()

        print(f"Sent -> {event.event_type}")