from monster_battle.iconfiguration import IConfiguration
import logging
import json


class FileConfiguration(IConfiguration):
    def __init__(self, filename):
        self._filename = filename
        self._logger = logging.getLogger('root')

    def get_configuration(self):
        configuration = None
        with open(self._filename) as json_data:
            configuration = json.load(json_data)
            self._logger.info(configuration)
        return configuration
