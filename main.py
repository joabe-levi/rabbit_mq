import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.basic.sender import BasicSender
from src.basic.consumer import BasicConsumer


def main():
    queue_name = 'minha_fila'

    sender = BasicSender(queue_name)
    sender.create_queue()

    consumer = BasicConsumer(queue_name)

    consumer.consume()
    sender.close_connection()


if __name__ == '__main__':
    main()
