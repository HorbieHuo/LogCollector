from persistence_adapter import common


class __fileAdapter__(common.LogAdapterObject):

    def __init__(self, *args, **kwargs):
        self.__enable__ = False
        self.__fileName__ = None

    def save(self, *args, **kwargs):
        if not self.__enable__:
            return
        with open(self.__fileName__, 'w+') as f:
            for r in args:
                data = self.getFormatMsg(r)
                f.write(data)
                f.write('\n')

    def config(self, *args, **kwargs):
        self.__fileName__ = kwargs.get('LOG_FILE', None)
        self.__enable__ = self.__fileName__ and kwargs.get('TO_FILE', False)


FileAdapter = __fileAdapter__()