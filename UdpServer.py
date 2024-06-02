#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 8888))
print("UDP bound on port 8888...")

while True:
    data, addr = s.recvfrom(1024)
    print("Receive from %s:%s" %(data,addr))
    if data == b"exit":
        s.sendto(b"Good bye!\n", addr)
        continue
    response=str(data)+" received from udpserver"
    s.sendto(response.encode("utf-8"), addr)
