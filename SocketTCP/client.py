import socket
import cv2

PORT = 10000
IP = '192.168.2.10'

cap = cv2.VideoCapture(0)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (IP, PORT)
sock.connect(server_address)
print('connecting to %s port %s' % server_address)

while True:
    try:
        _, frame = cap.read()
        frame = cv2.resize(frame, (120, 90))
        encoded = cv2.imencode('.jpg', frame)[1].tostring()
        sock.sendall(encoded)
    except Exception as e:
        print (e)
        break
sock.close()