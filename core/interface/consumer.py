from abc import ABC, abstractmethod


class IConsumer(ABC):
    
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
    def consume(self) -> None:
        """
            Starts consuming messages from the connected service.
            Example:
            def consume(self):
                self.channel.basic_consume(
                    queue=self.queue, on_message_callback=self.callback, auto_ack=True
                )
                self.channel.start_consuming()
        """
        raise NotImplementedError('Method must be implemented.')

    @abstractmethod
    def close_connection(self) -> None:
        """
            Closes the connection to the external service after consuming messages.
            Example:
            def close_connection(self):
                self.channel.close()
                self.connection.close()
        """
        pass
