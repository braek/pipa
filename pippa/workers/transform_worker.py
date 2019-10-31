from pippa.workers.base_worker import BaseWorker


class TransformWorker(BaseWorker):
    def run(self):
        while True:
            print('TRANSFORM WORKER')
