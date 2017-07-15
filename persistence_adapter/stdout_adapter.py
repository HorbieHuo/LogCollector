from persistence_adapter import common

class __stdoutAdapter__(common.LogAdapterObject):

    def __init__(self, *args, **kwargs):
        self.__enable__ = False

    def save(self, *args, **kwargs):
        if args:
            msg = self.getFormatMsg(args[0])
            if msg:
                print(msg)

    def config(self, *args, **kwargs):
        self.__enable__ = kwargs.get("STDOUT_ENABLE", False)
