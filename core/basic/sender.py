import sys, os, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core.interface.sender import ISender
import pika as rabbitmq
from config import settings


class BasicSender(ISender):

    def __init__(self, exchange, routind_key, queue) -> None:
        self._exchange = exchange
        self._routind_key = routind_key
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
            self._channel = rabbitmq.BlockingConnection(self.get_connection_parameters()).channel()

        except Exception as err:
            print(f"Error: {err}")

    def send_message(self, message):
        self._channel.basic_publish(
            exchange=self._exchange, 
            routing_key=self._routind_key, 
            body=json.dumps(message)
        )
        print(f'Message sent to queue: {self._queue}')

    def close_connection(self):
        if self._channel and self._channel.is_open:
            self._channel.close()

        if self._connection and self._connection.is_open:
            self._connection.close()


        print('Consumer closed.')
