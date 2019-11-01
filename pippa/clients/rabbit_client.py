from pika.exceptions import AMQPConnectionError
import pika
import json
from retry import retry


class RabbitClientException(Exception):
    pass


class RabbitClient(object):

    EXCHANGE_TYPE = 'direct'
    RAW_RECORDS_QUEUE = 'raw_records'
    STAGED_RECORD_QUEUE = 'staged_records'
    ERRORS_QUEUE = 'errors'

    def __init__(self, url, exchange, queues=[], prefetch_count=100):
        self._url = url
        self._queues = []
        for queue in queues:
            self._queues.append(f'{queue}_{self.RAW_RECORDS_QUEUE}_q'.lower())
            self._queues.append(f'{queue}_{self.STAGED_RECORD_QUEUE}_q'.lower())
            self._queues.append(f'{queue}_{self.ERRORS_QUEUE}_q'.lower())

        self._exchange = exchange
        self._prefetch_count = prefetch_count
        self._connection = None
        self._channel = None

    def disconnect(self):
        """
        Closes the channel and connection to RabbitMQ
        """
        if self._channel and self._channel.is_open:
            self._channel.stop_consuming()
        if self._connection and self._connection.is_open:
            self._connection.close()

    @retry(AMQPConnectionError, tries=5, delay=5)
    def connect(self):
        """
        Opens a connection to the configured RabbitMQ and initializes the configured queues
        """
        self.disconnect()
        self._connection = pika.BlockingConnection(pika.URLParameters(self._url))
        self._channel = self._connection.channel()
        self._channel.basic_qos(prefetch_count=self._prefetch_count)
        self._channel.exchange_declare(exchange=self._exchange, durable=True, exchange_type=self.EXCHANGE_TYPE)
        for queue in self._queues:
            self._channel.queue_declare(queue=queue, durable=True)
            self._channel.queue_bind(exchange=self._exchange, queue=queue)

    def publish(self, queue, message):
        while True:
            try:
                self._channel.basic_publish(
                    exchange=self._exchange,
                    routing_key=queue,
                    body=json.dumps(message)
                )
                break
            except Exception as e:
                self.connect()

    def publish_error(self, queue, message):
        self.publish(f'{queue}_{self.ERRORS_QUEUE}_q'.lower(), message)

    def ack(self, tag):
        while True:
            try:
                self._channel.basic_ack(delivery_tag=tag)
                break
            except Exception as e:
                self.connect()

    def consume(self, callback, queue=None):
        while True:
            queues = set([queue for queue in self._queues if queue != self.ERRORS_QUEUE] if queue is None else [queue])
            for queue in queues:
                self._channel.basic_consume(queue=queue, auto_ack=False, on_message_callback=callback)
            self._channel.start_consuming()
