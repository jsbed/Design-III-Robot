import os

from Robot.communication.base_station_client import BaseStationClient
from Robot.configuration.config import Config
from Robot.cycle.cycle import Cycle
from Robot.cycle.cycle_state import CycleState
from Robot.filler import country_repository_filler
from Robot.country.country_repository import CountryRepository
from Robot.country.flag_creator import FlagCreator


# Initiate configuration
Config().load_config()

# Fill Country repository
flags_file_path = os.path.join("Robot", "resources", "flags.csv")
country_repository_filler.fill_repository_from_file(flags_file_path)

# Start client
BaseStationClient().connect_socket()
BaseStationClient().wait_for_start_cycle_signal()

c = Cycle()
#c._state = CycleState.PUT_DOWN_CUBE
#c._flag_creator = FlagCreator(CountryRepository().get("Canada"))
#c._flag_creator.next_cube()
#c._flag_creator.next_cube()
#c._flag_creator.next_cube()
#c._next_state()
c.start_cycle()



