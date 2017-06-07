import socket
import pickle
import logging
import struct

if __name__ == "__main__":
    address = ('localhost', 11111)  
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
    s.bind(address)  
    print("start udp: localhost:11111")
    addr = ()
    while True:
        data = s.recv(4)
        # data, addr = s.recvfrom(20480)
        slen = struct.unpack(">L", data)[0]
        print(slen, data)
        data = s.recv(slen)
        while len(data) < slen:
            data = data + s.recv(slen - len(data))
        if not data:
            print("client has exist")
            break
        print("received: %s from %s type: %s" % (len(data), addr, type(data)))
        print(data)
        ss = pickle.loads(data)
        print(ss)
        print(logging.makeLogRecord(ss).getMessage())
    
    # s.close()
    # lr = logging.makeLogRecord({})
    # print(lr)
    # lrd = dict(lr.__dict__)
    # pk= pickle.dumps(lrd, 1)
    # print(pk)