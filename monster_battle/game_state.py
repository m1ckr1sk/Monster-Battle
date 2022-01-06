"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load criteria

"""


class GameState():
    """GameState

    This class contains the logic for the game state

    """

    def __init__(self):
        self._items = []
        self._rolls = []

    def set_items(self, items):
        """ Sets the games items
        Args:
            items (list): game items
        """
        self._items = items

    def get_items(self):
        """ Gets the games items
        """
        return self._items

    def set_rolls(self, rolls):
        """ Sets the games dice rolls
        Args:
            rolls (list): dice rolls
        """
        self._rolls = rolls

    def get_rolls(self):
        """ Gets the games dice rolls
        """
        return self._rolls
