import sys, os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from core.basic.basic_sender.sender import BasicSender


class AmazonBuilder:

    def __init__(self, exchange='amazon_exchange', queue='amazon_queue', routing_key=''):
        self._exchange = exchange
        self._queue = queue
        self._routing_key = routing_key
        self.sender = BasicSender(self._exchange, self._routing_key, self._queue)

    def bind_queue(self):
        try:
            self.sender._channel.exchange_declare(
                exchange=self._exchange, exchange_type='direct', durable=True
            )

            self.sender._channel.queue_declare(queue=self._queue, durable=True)
            self.sender._channel.queue_bind(
                exchange=self._exchange, queue=self._queue, routing_key=self._routing_key
            )

            print(f"Queue '{self._queue}' bound to exchange '{self._exchange}' with empty routing key.")
        except Exception as e:
            print(f"Error while binding queue: {e}")


    def build(self):
        self.bind_queue()
        print("AmazonBuilder setup complete. Ready to send messages.")
        return self.sender
