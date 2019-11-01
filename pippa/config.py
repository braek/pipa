CONFIG = dict()
CONFIG['RABBIT_QUEUES'] = 'audi,bmw,mercedes'
CONFIG['RABBIT_USERNAME'] = 'pippa'
CONFIG['RABBIT_HOSTNAME'] = 'localhost'
CONFIG['RABBIT_PASSWORD'] = 'T7j8d8Af'
CONFIG['RABBIT_EXCHANGE'] = 'pippa'
CONFIG['RABBIT_PORT'] = 8802
CONFIG['RABBIT_PREFETCH_COUNT'] = 10
CONFIG['RABBIT_URL'] = 'amqp://{username}:{password}@{hostname}:{port}/{exchange}'.format(
    username=CONFIG['RABBIT_USERNAME'],
    password=CONFIG['RABBIT_PASSWORD'],
    hostname=CONFIG['RABBIT_HOSTNAME'],
    port=CONFIG['RABBIT_PORT'],
    exchange=CONFIG['RABBIT_EXCHANGE']
)
