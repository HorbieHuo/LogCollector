
import pickle
import logging
import setting as CONFIG
from queue import Q
from persistence_adapter import SAVERS
from persistence_adapter import InitAdapter

def Save(*args, **kwargs):
    event = kwargs.get('event', None)
    if not event:
        return
    InitAdapter(**CONFIG.__dict__)
    while True:
        if Q.count <= 0:
            event.clear()
            event.wait(2)
        datas, count = Q.get()
        if count <= 0:
            continue
        for data in datas:
            r = __assembleRecordLog__(data)
            if r:
                for s in SAVERS:
                    s.save(r)

def __formatLog__(*args):
    pass

def __assembleRecordLog__(data):
    try:
        recordDict = pickle.loads(data[4:])
        return logging.makeLogRecord(recordDict)
    except Exception as e:
        print("__assembleRecordLog__: %s" % (e))
        return None

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
