import socket


PORT = 10000
IP = '132.203.92.207'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, PORT)

print('connecting to %s port %s' % server_address)

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)
        message = input('Message: ')
        
        if message=='quit':
            break
        sock.sendall(bytes(message, "utf-8"))
    except Exception as e:
        print (e)
        break
sock.close()