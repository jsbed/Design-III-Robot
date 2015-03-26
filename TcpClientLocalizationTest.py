import zmq

from Robot.communication.localization import localization_response, localization_request
from Robot.configuration.config import Config


Config().load_config()


# Create a TCP/IP socket
context = zmq.Context()
socket = context.socket(zmq.DEALER)  # @UndefinedVariable
url = "tcp://{}:{}".format(
    Config().get_base_station_communication_ip(),
    Config().get_base_station_communication_port())
socket.connect(url)
print('connecting to ' + url)


socket.send(
    bytes(localization_request.create_robot_localization_request(), "utf-8"))
print("waiting")
a = socket.recv().decode("utf-8")
print("received")
loc = localization_response.create_localization_from_localization_response(a)
print(loc.position)
print(loc.orientation)
print(loc.unknown)
