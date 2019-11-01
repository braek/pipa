from pippa.workers.base_worker import BaseWorker


class LoadWorker(BaseWorker):
    def run(self):
        print('LOAD WORKER')
