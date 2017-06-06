
from file_adapter import FileAdapter

SAVERS = [FileAdapter, ]

def InitAdapter(*args, **kwargs):
    for s in SAVERS:
        s.config(*args, **kwargs)