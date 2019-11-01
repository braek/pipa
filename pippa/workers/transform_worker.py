from pippa.workers.base_worker import BaseWorker


class TransformWorker(BaseWorker):
    def run(self):
        print('TRANSFORM WORKER')
