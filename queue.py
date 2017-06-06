
import setting

all = ['Q', ]

class __QUEUE__(object):
    def __init__(self, *args, **kwargs):
        self.__queue__ = []
        self.__count__ = 0

    def get(self):
        q = self.__queue__
        c = self.__count__
        self.__queue__ = []
        self.__count__ = 0
        return q, c

    def append(self, data):
        if self.__count__ > setting.CACHE_MAX_LOG_COUNT:
            return False
        self.__queue__.append(data)
        self.__count__ += 1
        return True
    
    def count(self):
        return self.__count__

Q = __QUEUE__()