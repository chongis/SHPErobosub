#!/usr/bin/env python3
import socket, time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

timeout = 10.0

print("Client Starting")
start = time.time()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while (time.time() - start < timeout):
        #s.sendall(b'Hello, world')
        data = s.recv(4096)
        if not data:
            break
        print('Received Reading: ' + data.decode("utf-8"))
    s.close()
print("Client Shutting Down...")
#print('Received', repr(data)) # Print can write to a file??!!

"""
import time
print("Client timer testing")

start = time.time()
while (True):
    if (time.time()-start) > 5.0:
        print("5 seconds have passed, exiting...")
        raise SystemExit
#end = time.time()
#print(end-start)
"""