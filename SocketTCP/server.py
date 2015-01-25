import socket
import cv2
import numpy


PORT = 10000
IP = '192.168.2.22'
BUFFER_SIZE = 1024000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, PORT)

print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    # Find connections
    connection, client_address = sock.accept()
    try:
        data = connection.recv(BUFFER_SIZE)
        nparr = numpy.fromstring(data, numpy.uint8)
        img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow("RGB", img_np)

    except:
        connection.close()