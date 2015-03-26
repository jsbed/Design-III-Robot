import socket


PORT = 3000
IP = '127.0.0.1'
BUFFER_SIZE = 999

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (IP, PORT)

print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

connection, _ = sock.accept()

while True:
    # Find connections
    try:
        data = connection.recv(BUFFER_SIZE)
        print(data)

    except Exception as e:
        print(str(e))
        connection.close()
        connection, _ = sock.accept()