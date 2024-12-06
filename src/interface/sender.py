from abc import ABC, abstractmethod


class ISender(ABC):

    @abstractmethod
    def get_connection(self) -> None:
        """
            Establishes the connection to the RabbitMQ service.
            Example:
            def get_connection(self):
                parameters = pika.ConnectionParameters(host='localhost', port=5672)
                self._connection = pika.BlockingConnection(parameters)
                self._channel = self.connection.channel()
                return self._channel
        """
        raise NotImplementedError('Method must be implemented.')

    @abstractmethod
    def send_message(self, message: str) -> None:
        """
        Sends a message to the connected service.
        Example:
            def send_message(self, message):
                self.channel.basic_publish(
                    exchange='', routing_key=self.queue, body=message
                )
        """
        raise NotImplementedError('Method must be implemented.')

    @abstractmethod
    def close_connection(self) -> None:
        """
        Closes the connection to the RabbitMQ service.
        Example:
            def close_connection(self):
                self.channel.close()
                self.connection.close()
        """
        raise NotImplementedError('Method must be implemented.')
