import os

HOST_IP = os.environ.get("HOST_IP", "localhost")
UDP_IP = os.environ.get("UDP_IP", HOST_IP)
UDP_PORT = os.environ.get("UDP_PORT", 46739)
UDP_MAX_BITS_RECV_ONE = os.environ.get("UDP_MAX_BITS_RECV_ONE", 10240)

CACHE_MAX_LOG_COUNT = 1024