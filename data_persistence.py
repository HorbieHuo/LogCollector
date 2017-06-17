
import pickle
import logging
from queue import Q
from persistence_adapter import SAVERS

def Save():
    while True:
        if Q.count <= 0:
            pass
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