import abc


class BaseWorker(object):

    @abc.abstractmethod
    def run(self):
        """
        You should implement this method in a subclass extending the BaseWorker.
        """
        pass
