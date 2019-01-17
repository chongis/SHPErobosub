# Files is going to be done in two parts, the socket connection
# and the directory/file manipulation. This second part should
# write, read, send, receive, and list all the files. 
import os
# Relevant os methods: getcwd(), chdir(), open(same as c), read(),
# write(), os.sendfile()!!!
print(os.getcwd())

# it seems that sendfile(out,in,offset,count) can use a socket as an fd, EOF == 0,
# the number of bytes sent
# b"abcde".decode("utf-8")
# socket.fileno() return file descriptor

# Copy files
def test():
    filein = os.open("./rfile.txt",os.O_RDONLY);
    textin = os.read(filein,4096);
    print(textin.decode("utf-8"))
    print(textin)
    fileout = os.open("./newfile.txt",os.O_CREAT | os.O_WRONLY);
    written = os.write(fileout,textin);
    os.close(filein)
    os.close(fileout)


def socket_test():
    import socket

    HOST = '127.0.0.1'
    PORT = 3333        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        filein = os.open("./bigtest.txt",os.O_RDONLY);
        sent = os.sendfile(s.fileno(),filein,None,4069)
        while(sent):
            sent = os.sendfile(s.fileno(),filein,None,4069)
        os.close(filein)
        s.close()

while (True):
    socket_test()
