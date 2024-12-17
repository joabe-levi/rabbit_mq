import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import pika as rabbitmq
from config import settings
from core.interface.consumer import IConsumer


class BasicConsumer(IConsumer):

    def __init__(self, queue) -> None:
        self._queue = queue
        self.get_connection()

    def get_connection_parameters(self):
        return rabbitmq.ConnectionParameters(
            host=settings.host,
            port=settings.port,
            credentials=rabbitmq.PlainCredentials(
                username=settings.username, password=settings.password
            )
        )

    def get_connection(self):
        try:
            self._connection = rabbitmq.BlockingConnection(self.get_connection_parameters())
            self._channel = self._connection.channel()
            self._channel.queue_declare(queue=self._queue, durable=True)
        except Exception as err:
            print(f"Unable to connect to the consumer: {err}")

    def callback(self, ch, method, properties, body):
        print(f"Message received: {body.decode()}")

    def consume(self):
        try:
            self._channel.basic_consume(
                queue=self._queue, on_message_callback=self.callback, auto_ack=True
            )
            print(f"Waiting messages in queue: {self._queue}...")
            self._channel.start_consuming()

        except KeyboardInterrupt:
            self.close_connection()

    def close_connection(self):
        if self._channel and self._channel.is_open:
            self._channel.close()

        if self._connection and self._connection.is_open:
            self._connection.close()

        print('Consumer closed.')
