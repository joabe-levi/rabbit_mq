import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from basic.sender import BasicSender


class AmazonBuilder:

    def __init__(self):
        self._exchange = 'amazon_exchange'
        self._queue = 'amazon_queue'
        self._routind_key = ''
        self.sender = BasicSender(self._exchange, self._routind_key, self._queue)
