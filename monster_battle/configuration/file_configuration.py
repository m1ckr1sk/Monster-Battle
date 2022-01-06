# -*- coding: utf-8 -*-
"""Configuration.

This module is the main configuration module and handles the
logic to load a predefined configuration into the engine.

Todo:
    * Think of better way to load criteria

"""
import logging
import json
from monster_battle.configuration.iconfiguration import IConfiguration


class FileConfiguration(IConfiguration):
    """FileConfiguration.

    This class loads a rules configuration from a file.

    """

    def __init__(self, filename):
        self._filename = filename
        self._logger = logging.getLogger('root')

    def get_configuration(self):
        """Get configuration from file.
        """
        configuration = None
        with open(self._filename, "r", encoding="utf-8") as json_data:
            configuration = json.load(json_data)
            self._logger.debug(configuration)
        return configuration
