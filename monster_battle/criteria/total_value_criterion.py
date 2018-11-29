"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
import logging
from monster_battle.criteria.icriterion import ICriterion


class TotalValueCriterion(ICriterion):
    """Total value rule.
    This rule passes if the sum value of all rolls is greater than
    the required value. The number of chances is the rolls that contribute
    to the total.
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

            self._logger.info("running total value rule requires %s",
                              required_value)
            self._logger.info("running total value rule. Value is %s..",
                              sum(game_state.get_rolls()
                                  [:self._number_of_chances]))
            if sum(
                    game_state.get_rolls()[:self._number_of_chances]) >= \
                    required_value:
                self._result = "True"

    def is_match(self, game_state):
        """Can the rule run?.
        Args:
            game_state (GameState): The game state to assess
        """
        return len(game_state.get_rolls()) >= self._number_of_chances

    def criteria_state(self):
        """Get the last state of the criterion"""
        return self._result
