import zmq

PORT = 3000
ADDRESS = "127.0.0.1"


def up():
    print("up command")


def down():
    print("down command")


def left():
    print("left command")


def right():
    print("right command")


def rotate_right():
    print("rotate-right command")


def rotate_left():
    print("rotate-left command")


context = zmq.Context()
socket = context.socket(zmq.DEALER)
url = "tcp://{}:{}".format(ADDRESS, PORT)
socket.bind(url)
print("Listening on", url)

while True:
    #  Wait for next request from client
    message = socket.recv().decode("utf-8")

    if message == "up":
        up()
    elif message == "down":
        down()
    elif message == "left":
        left()
    elif message == "right":
        right()
    elif message == "rotate-right":
        rotate_right()
    elif message == "rotate-left":
        rotate_left()
    else:
        print("Other message", message)
