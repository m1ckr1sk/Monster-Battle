"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
import logging
from monster_battle.rules.irule import IRule


class GreaterThanRule(IRule):
    """Exact Match Rule

    This class implements a rule which will pass if any roll in the
    number of chances is greater the required value.

    """
    def __init__(self, number_of_chances, required_value):
        self._number_of_chances = number_of_chances
        self._required_value = required_value
        self._result = "not run"
        self._logger = logging.getLogger('root')

    def execute(self, game_state, input_gatherer):
        """Execute the rule.
        Args:
            game_state (GameState): The game state to assess
        """
        self._result = "False"
        if len(game_state.get_rolls()) >= self._number_of_chances:
            if self._required_value == "user":
                required_value = input_gatherer.get_input(
                    "please enter required value for rule:")
            else:
                required_value = int(self._required_value)

            self._logger.info("Max rule requires %s",
                              required_value)
            self._logger.info("Player highest throw %s",
                              max(game_state.get_rolls()
                                  [:self._number_of_chances]))

            if max(game_state.get_rolls()[:self._number_of_chances]) >= \
                    required_value:
                self._result = "True"

    def is_match(self, game_state):
        """Can the rule run?.
        Args:
            game_state (GameState): The game state to assess
        """
        return len(game_state.get_rolls()) >= self._number_of_chances

    def rule_state(self):
        """Get the last state of the rule"""
        return self._result
