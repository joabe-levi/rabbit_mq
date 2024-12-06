import time
from sender import Sender
from consumer import Consumer

def main():
    queue_name = 'minha_fila'

    sender = Sender(queue_name)
    sender.create_queue()  # Cria a fila no RabbitMQ

    consumer = Consumer(queue_name)

    for i in range(5):
        message = f"Mensagem {i+1}"
        sender.send_message(message)
        time.sleep(1)

    consumer.consume()
    sender.close_connection()

if __name__ == '__main__':
    main()
