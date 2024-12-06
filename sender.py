import pika as rabbit


class Sender:

    def __init__(self, queue) -> None:
        self._queue = queue
        self._get_connection()

    def _get_connection(self):
        try:
            self._connection = rabbit.BlockingConnection(rabbit.ConnectionParameters('localhost'))
            self._channel = self._connection.channel()
        except Exception as err:
            print(f"Error: {err}")

    def show_queue(self):
        return self._queue
    
    def create_queue(self):
        self._channel.queue_declare(queue=self._queue, durable=True)
        print(f'Queue ({self._queue}) created.')

    def send_message(self, message):
        self._channel.basic_publish(
            exchange='',
            routing_key=self._queue,
            body=message,
            properties=rabbit.BasicProperties(delivery_mode=2)
        )
        print(f'Message sent to queue: {self._queue}')

    def close_connection(self):
        if self._channel and self._channel.is_open:
            self._channel.close()
            print('Channel closed.')

        if self._connection and self._connection.is_open:
            self._connection.close()
            print('Connection closed.')
