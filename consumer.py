import pika as rabbit


class Consumer:

    def __init__(self, queue) -> None:
        self._queue = queue
        self._get_connection()

    def _get_connection(self):
        try:
            self._connection = rabbit.BlockingConnection(rabbit.ConnectionParameters('localhost'))
            self._channel = self._connection.channel()
            self._channel.queue_declare(queue=self._queue, durable=True)
        except Exception as err:
            print(f"Error: {err}")

    def callback(self, ch, method, properties, body):
        print(f"Mensagem recebida: {body.decode()}")

    def consume(self):
        self._channel.basic_consume(queue=self._queue, on_message_callback=self.callback, auto_ack=True)
        print(f"Waiting messages in queue: {self._queue}...")
        self._channel.start_consuming()

    def close_connection(self):
        if self._channel and self._channel.is_open:
            self._channel.close()
            print('Channel closed.')

        if self._connection and self._connection.is_open:
            self._connection.close()
            print('Connection closed.')
