
from queue import Q
from persistence_adapter import SAVERS

def Save():
    while True:
        if Q.count <= 0:
            pass
        datas, count = Q.get()
        if count <= 0:
            continue

def __formatLog__(*args):
    pass