from pippa.workers import Worker


class LoadWorker(Worker):
    def run(self):
        while True:
            print('LOAD WORKER')
