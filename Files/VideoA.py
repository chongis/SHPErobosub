import numpy as np
from scipy.misc import imread, imsave, imresize
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image

def resize_image(a):
    basewidth = 300
    ##change this according to the camera's resulution 
    
    img = Image.open(a)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save(a)
    

def send_resized_image(a):
    #a is a string naming a path to the location of the image
    import socket

    img = resize_image(a)
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
        

##resize_image('scotland1.jpg')
