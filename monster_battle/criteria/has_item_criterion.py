"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
import logging
from monster_battle.criteria.icriterion import ICriterion


class HasItemCriterion(ICriterion):
    """Has item rule.
    This rule allows a config to test if the player has s specified
    item.
    """
    def __init__(self, item):
        self._item = item
        self._result = "not run"
        self._logger = logging.getLogger('root')

    def execute(self, game_state, input_gatherer):  # pylint: disable=unused-argument # noqa E501
        """Execute the rule.
        Args:
            game_state (GameState): The game state to assess
        """
        self._logger.info("executing has item rule...")
        if self._item in game_state.get_items():
            self._logger.info("has item rule has found required item...")
            self._result = "True"
        else:
            self._logger.info("has item rule cannot find required item...")
            self._result = "False"

    def is_match(self, game_state):  # pylint: disable=unused-argument
        """Can the rule run?.
        Args:
            game_state (GameState): The game state to assess
        """
        self._logger.info("checking if has item rule can run...")
        return True

    def criteria_state(self):
        """Get the last state of the criterion"""
        return self._result
