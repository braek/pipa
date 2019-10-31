from pippa.workers import Worker


class ExtractWorker(Worker):
    def run(self):
        while True:
            print('EXTRACT WORKER')
