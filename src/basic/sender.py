from src.interface.sender import ISender
import pika as rabbitmq
from config import settings


class BasicSender(ISender):

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
            self._channel = rabbitmq.BlockingConnection(self.get_connection_parameters()).channel()

        except Exception as err:
            print(f"Error: {err}")

    def close_connection(self):
        if self._channel and self._channel.is_open:
            self._channel.close()
            print('Channel closed.')

        if self._connection and self._connection.is_open:
            self._connection.close()
            print('Connection closed.')
