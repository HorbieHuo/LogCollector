class Queue(object):
    def __init__(self, *args, **kwargs):
        self.__queue__ = []
        self.__count__ = 0

    def get(self):
        q = self.__queue__
        self.__queue__ = []
        self.__count__ = 0
        return q

    def append(self, data):
        self.__queue__.append(data)
        self.__count__ += 1
        return True