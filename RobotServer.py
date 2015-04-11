import os
import shutil

from Robot.communication.base_station_client import BaseStationClient
from Robot.configuration.config import Config
from Robot.cycle.cycle import Cycle
from Robot.filler import country_repository_filler

ss_folder_name = "run_screenshots"

# Create/Clear screenshot folder
if os.path.isdir(ss_folder_name):
    shutil.rmtree(ss_folder_name)

os.makedirs(ss_folder_name)


# Initiate configuration
Config().load_config()

# Fill Country repository
country_repository_filler.fill_repository()

# Start client
BaseStationClient().connect_socket()
BaseStationClient().wait_for_start_cycle_signal()

# Start the AI cycle
Cycle().start_cycle()
