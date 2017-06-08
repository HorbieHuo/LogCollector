
import logging
import pickle
from queue import Q
from persistence_adapter import SAVERS

def Save(*args, **kwargs):
    event = kwargs.get('event', None)
    if not event:
        return
    while True:
        if Q.count <= 0:
            event.clear()
            event.wait(2)
        datas, count = Q.get()
        if count <= 0:
            continue
        logRecords = __constructLogRecords__(datas)
        for s in SAVERS:
            s.save(*logRecords)

def __formatLog__(*args):
    pass

def __constructLogRecords__(datas):
    logRecords = []
    for data in datas:
        try:
            logRecords.append(
                logging.makeLogRecord(pickle.loads(data))
            )
        except Exception as e:
            print(e)
    return logRecords