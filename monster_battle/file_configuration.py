from monster_battle.iconfiguration import IConfiguration
import json


class FileConfiguration(IConfiguration):
    def __init__(self, filename):
        self._filename = filename

    def get_configuration(self):
        configuration = None
        with open(self._filename) as json_data:
            configuration = json.load(json_data)
            print(configuration)
        return configuration
