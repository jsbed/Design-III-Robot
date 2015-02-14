from configparser import ConfigParser

from Robot.utilities.singleton import Singleton


CONFIG_FILE_NAME = "config.ini"

PARAMETER_ATLAS_URL = "AtlasUrl"
PARAMETER_KINECT_CONNECTION_PORT = "KinectConnectionPort"


class Config(metaclass=Singleton):

    def __init__(self):
        self._parser = ConfigParser()
        self._parameters = {}

    def load_config(self):
        self._parser.read(CONFIG_FILE_NAME)
        self._parameters = self._parser.defaults()

    def get_atlas_url(self):
        return self._get_parameter(PARAMETER_ATLAS_URL)

    def get_kinect_connection_port(self):
        return self._get_parameter(PARAMETER_KINECT_CONNECTION_PORT)

    def get_country_data_path(self):
        return self._get_parameter('CountryDataPath')

    def _get_parameter(self, parameter):
        if parameter.lower() in self._parameters:
            return self._parameters[parameter.lower()]
        else:
            raise Exception("'{}' parameter is not in the config file".
                            format(parameter))
