
<<<<<<< HEAD
import pickle
import logging
=======
import logging
import pickle
>>>>>>> 0b42f9fbdeadc7dbd2abf468459d5330d8fb8949
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
<<<<<<< HEAD
        for data in datas:
            r = __assembleRecordLog__(data)
            if r:
                for s in SAVERS:
                    s.save(r)
=======
        logRecords = __constructLogRecords__(datas)
        for s in SAVERS:
            s.save(*logRecords)
>>>>>>> 0b42f9fbdeadc7dbd2abf468459d5330d8fb8949

def __formatLog__(*args):
    pass

<<<<<<< HEAD
def __assembleRecordLog__(data):
    try:
        recordDict = pickle.loads(data[4:])
        return logging.makeLogRecord(recordDict)
    except Exception as e:
        print("__assembleRecordLog__: %s" % (e))
        return None
=======
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
>>>>>>> 0b42f9fbdeadc7dbd2abf468459d5330d8fb8949
