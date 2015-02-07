import os

from Configuration.Config import Config
from Filler import CountryRepositoryFiller


# Initiate configuration
Config().loadConfig()

# Fill Country repository
flags_file_path = os.path.join("resources", "flags.csv")
CountryRepositoryFiller.fill_repository_from_file(flags_file_path)
