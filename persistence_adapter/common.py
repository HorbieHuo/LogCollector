import logging

class LogAdapterObject(object):

    def __init__(self, *args, **kwargs):
        self.__formatString__=kwargs.get('LOG_FROMAT_STRING', "")
        self.__formater__=None
        if self.__formatString__:
            self.__formater__ = logging.Formatter(fmt=self.__formatString__)

    def getFormatMsg(logRecord):
        if not logRecord or not self.__formater__:
            return ""
        return self.__formater__.format(logRecord)