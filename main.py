from core.basic.consumer import BasicConsumer


def main():
    try:
        queue_name = 'amazon_queue'
        consumer = BasicConsumer(queue_name)
        consumer.consume()
        
    finally:
        consumer.close_connection()
        print('Consumer closed.')

if __name__ == '__main__':
    main()
