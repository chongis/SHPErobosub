#!/usr/bin/env python3

import socket, time, random

timeout = 100.0
def sensorInfo(timeDelay = .5):
    """
    Returns Psuedo sensor info for testing purposes,
    however the interface should be exactly the same as this
    function.
    """
    cycle = time.time()
    while (time.time() - cycle < timeDelay):
        pass
    return random.randint(1,10000)

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

start = time.time()
print("Server Starting")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    #s.settimeout(4.0)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while (time.time() - start < timeout): # Transmit data for 4 seconds 
            #data = conn.recv(4096)
            data = str(sensorInfo())
            #if not data:
            #    break
            print(data)
            conn.sendall(data.encode('utf-8'))
print("Server Demo Done\n")