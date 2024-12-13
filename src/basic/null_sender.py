import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from interface.sender import ISender

from src.interface.sender import ISender


class BasicNullSender(ISender):

    def __init__(self, exchange, routind_key, queue) -> None:
        self._exchange = None
        self._routind_key = None
        self._queue = None

        self.get_connection()

    def get_connection(self):
        print("No connection configured. Connection not established.")
        self._channel = None

    def send_message(self, message):
        print('No sender configured. Message not sent.')

    def close_connection(self):
        print("No connection to close.")
