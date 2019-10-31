from pippa.workers import Worker


class TransformWorker(Worker):
    def run(self):
        while True:
            print('TRANSFORM WORKER')
