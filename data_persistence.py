
import logging
import pickle
from queue import Q
from persistence_adapter import SAVERS

def Save():
    while True:
        if Q.count <= 0:
            pass
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