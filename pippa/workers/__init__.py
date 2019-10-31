import abc


class Worker(object):
    @abc.abstractmethod
    def run(self):
        pass
