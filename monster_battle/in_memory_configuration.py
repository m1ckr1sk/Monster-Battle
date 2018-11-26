from monster_battle.iconfiguration import IConfiguration
import logging


class InMemoryConfiguration(IConfiguration):

    def __init__(self):
        self._logger = logging.getLogger('root')
        self._logger.info("Creating in memory config")

    def get_configuration(self):
        configuration = {}
        monsters = []
        monster = {}
        monster["name"] = "cyclops"
        monster["rule"] = "C1 and C2"

        conditions = []
        condition1 = {}
        condition1["type"] = "item"
        condition1["required_item"] = "sword"
        condition1["name"] = "C1"
        conditions.append(condition1)

        condition2 = {}
        condition2["type"] = "total value"
        condition2["number_of_chances"] = 2
        condition2["required_value"] = 10
        condition2["name"] = "C2"
        conditions.append(condition2)

        monster["conditions"] = conditions
        monsters.append(monster)
        configuration["monsters"] = monsters
        return configuration
