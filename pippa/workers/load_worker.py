from pippa.workers.base_worker import BaseWorker


class LoadWorker(BaseWorker):
    def run(self):
        while True:
            print('LOAD WORKER')
