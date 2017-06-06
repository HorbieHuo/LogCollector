
import threading

from udp import Udp
from data_persistence import Save

if __name__ == "__main__":
    netThread = threading.Thread(
        target=Udp,
        args=(),
        kwargs=None,
    )
    dataThread = threading.Thread(
        target=Save,
        args=(),
        kwargs=None,
    )
    dataThread.start()
    netThread.start()
    netThread.join()
    dataThread.join()