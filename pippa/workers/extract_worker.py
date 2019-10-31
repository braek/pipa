from pippa.workers.base_worker import BaseWorker


class ExtractWorker(BaseWorker):
    def run(self):
        while True:
            print('EXTRACT WORKER')
