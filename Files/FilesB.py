# Server 
import socket, os

HOST = '127.0.0.1' 
PORT = 3333

fileno = 0
namefile = "./filenum"
filename = ""

def socket_test():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while (True):
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(4069)
                    if not data:
                        break
                    print("Writing File")
                    filename = namefile + str(fileno) + ".txt"
                    fileout = os.open(filename, os.O_CREAT | os.O_WRONLY)
                    written = os.write(fileout,data)
                    print(written)
                    while(written):
                        data = conn.recv(4069)
                        written = os.write(fileout,data)    
                    os.close(fileout)
                    print("Done Writing")
                    fileno+=1

socket_test()     
