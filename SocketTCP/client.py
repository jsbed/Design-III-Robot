import socket
import cv2

PORT = 10000
IP = '192.168.2.22'

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
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("GRAY", gray)
        cv2.imshow("RGB", frame)
        c = cv2.waitKey(1)
        if c == 27: #to quit, the 'ESC' key is pressed
            exit()

        sock.sendall(bytes(frame, "utf-8"))
    except Exception as e:
        print (e)
        break
sock.close()