import socket

import setting
from queue import Q

if __name__ == "__main__":
    address = ('localhost', 11111)  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.bind(address)
    print "start udp: localhost:11111"
    while True:
        data, addr = s.recvfrom(2048)
        if not data:  
            print "client has exist"  
            break  
        print "received:", len(data), "from", addr, "type:", type(data)
    
    s.close()

def Udp(*args, **kwargs):
    '''
    udp
    '''
    event = kwargs.get('event', None)
    if not event:
        return
    address = (setting.UDP_IP, setting.UDP_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.bind(address)
    print("start udp: %s:%s" % address)
    while True:
        data, addr = s.recvfrom(setting.UDP_MAX_BITS_RECV_ONE)
        if not data:
            print "client has exist"
            break
        Q.append(data)
        if not event.is_set():
            event.set()
        print "received:", len(data), "from", addr, "type:", type(data)
    s.close()