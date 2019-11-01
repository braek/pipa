from pippa.clients.rabbit_client import RabbitClient
from pippa.config import CONFIG

rabbit_client = RabbitClient(
    url=CONFIG['RABBIT_URL'],
    exchange=CONFIG['RABBIT_EXCHANGE'],
    queues=CONFIG['RABBIT_QUEUES'].split(','),
    prefetch_count=CONFIG['RABBIT_PREFETCH_COUNT']
)
rabbit_client.connect()
rabbit_client.publish_error('mercedes', {'error': 'Je te flouppe Fli'})
rabbit_client.disconnect()
