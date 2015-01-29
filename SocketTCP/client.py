import socket
import cv2
import time

PORT = 3000
IP = '192.168.0.25'

cap = cv2.VideoCapture(cv2.CAP_OPENNI)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (IP, PORT)
sock.connect(server_address)
print('connecting to %s port %s' % server_address)

cap.read()
time.sleep(1)

while True:
    try:
        cap.grab()
        flag, frame = cap.retrieve(None, cv2.CAP_OPENNI_BGR_IMAGE)
        #cv2.imshow("nofucksgiven", frame)
        frame = cv2.resize(frame, (560, 420))
        cv2.imshow("nofucksgiven", frame)
        if not flag: continue
        encoded = cv2.imencode('.jpg', frame)[1].tostring()
        sock.sendall(encoded)
    except Exception as e:
        print (e)
        break
sock.close()
