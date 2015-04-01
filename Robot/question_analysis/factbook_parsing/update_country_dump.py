from pathlib import Path
import os
import shutil

country_data_dir = Path('./factbook/geos')
for country_file in country_data_dir.iterdir():
    if country_file.is_dir():
        shutil.rmtree(country_file.as_posix())

    elif country_file.suffix != '.html':
        os.remove(country_file.as_posix())
