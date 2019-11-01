from pippa.workers.base_worker import BaseWorker


class ExtractWorker(BaseWorker):
    def run(self):
        print('EXTRACT WORKER')
