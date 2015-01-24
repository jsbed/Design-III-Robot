import socket


PORT = 10000
IP = '132.203.92.207'
BUFFER_SIZE = 999

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
        print(data)

    except:
        connection.close()