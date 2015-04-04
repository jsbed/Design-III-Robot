from Robot.communication.base_station_client import BaseStationClient
from Robot.configuration.config import Config
from Robot.cycle.cycle import Cycle
from Robot.filler import country_repository_filler


# Initiate configuration
Config().load_config()

# Fill Country repository
country_repository_filler.fill_repository()

# Start client
BaseStationClient().connect_socket()
BaseStationClient().wait_for_start_cycle_signal()

# Start the AI cycle
Cycle().start_cycle()
