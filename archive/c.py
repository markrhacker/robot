#client server
# this run on the comoputer gather data
# the less powerful one

import socket
import time
import cv2
from PIL import Image
import pickle

datapacket = "0101101100101001110001000100000011111011010101001"


def getCamImage():
    image = cv2.imread("/Users/markhacker/Desktop/robot/cam.jpg")
    height, width = image.shape[:2]
    width = int(width/1.4)
    height = int(height/1.4)
    image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
    return image, width, height

image, width, height = getCamImage()

def PackData():
    print("packing data.....")
    data = pickle.dumps(image, 0)
    size = len(data)
    print(size)
    #print ("<X>",image,"<X>")


# create a socket and bind socket to the host
print("Socket Init")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.16', 8002)) 
print("Socket done")

try:
    while True:
        PackData()
        # send data to the host every 0.5 sec
        #client_socket.send((datapacket))
        client_socket.send((image))
        time.sleep(0.5)
finally:
    client_socket.close()