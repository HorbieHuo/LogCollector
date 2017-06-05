import socket

import setting

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

def Udp():
    '''
    udp
    '''
    address = (setting.UDP_IP, setting.UDP_PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.bind(address)  
    print "start udp: localhost:11111"
    while True:
        data, addr = s.recvfrom(setting.UDP_MAX_BITS_RECV_ONE)
        if not data:
            print "client has exist"
            break
        print "received:", len(data), "from", addr, "type:", type(data)
    s.close()