import socket
import cv2
import numpy

PORT = 10000
IP = '192.168.2.10'

cap = cv2.VideoCapture(0)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, PORT)

print('connecting to %s port %s' % server_address)

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        ret, frame = cap.read()
        frame = cv2.resize(frame, (120, 90))
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("GRAY", frame)
        c = cv2.waitKey(1)
        if c == 27: #to quit, the 'ESC' key is pressed
            exit()

        encoded = cv2.imencode('.jpg', frame)[1].tostring()
        sock.sendall(encoded)
        nparr = numpy.fromstring(encoded, numpy.uint8)
        cv2.imshow("RGB", cv2.imdecode(nparr, cv2.IMREAD_COLOR))
    except Exception as e:
        print (e)
        break
sock.close()