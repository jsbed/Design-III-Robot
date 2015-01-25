import socket
import cv2
import numpy


PORT = 10000
IP = '192.168.2.10'
BUFFER_SIZE = 10000


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (IP, PORT)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)


while True:
    try:
        data = sock.recv(BUFFER_SIZE)
        nparr = numpy.fromstring(data, numpy.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        c = cv2.waitKey(1)
        if c == 27:
            exit()
        cv2.imshow("RGB", img_np)

    except Exception as e:
        print(e)
