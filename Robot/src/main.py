import os

from Filler.CountryRepositoryFiller import CountryRepositoryFiller


# Fill Country repository
flags_file_path = os.path.join("resources", "flags.csv")
CountryRepositoryFiller().fill_repository_from_file(flags_file_path)
