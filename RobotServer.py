import os

from Robot.communication.base_station_client import BaseStationClient
from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.filler import country_repository_filler


# Initiate configuration
Config().load_config()

# Fill Country repository
flags_file_path = os.path.join("Robot", "resources", "flags.csv")
country_repository_filler.fill_repository_from_file(flags_file_path)

# Start client
BaseStationClient().connect_socket()

t = TCPClient(Config().get_base_station_ip(),
              Config().get_base_station_signal_server_port())

# t.connect_socket()
# print(t.get_data())
print(BaseStationClient().get_data())
