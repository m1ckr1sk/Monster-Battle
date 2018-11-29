"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load criterions

"""
import logging
from monster_battle.criteria.icriterion import ICriterion


class BoundedMatchCriterion(ICriterion):
    """Bounded Match Criterion

    This class implements a rule which will pass if any roll in the
    number of chances matches the required value +/- the boundary offset.

    """
    def __init__(self, number_of_chances, required_value, boundary_offset):
        self._number_of_chances = number_of_chances
        self._required_value = required_value
        self._boundary_offset = boundary_offset
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
                required_value = input_gatherer.get_number_input(
                    "please enter required value for rule:")
            else:
                required_value = int(self._required_value)

            required_values = self.get_expanded_range(required_value)

            self._logger.info("Bounded match rule requires %s",
                              required_values)
            self._logger.info("Player has thrown %s",
                              game_state.get_rolls()[:self._number_of_chances])
            if any(x in required_values for x in game_state.get_rolls()):
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

    def get_expanded_range(self, required_value):
        """Take the required value and add the other values that will match
        if we apply the offset"""
        required_values = []
        for val in range(required_value - self._boundary_offset,
                         required_value + self._boundary_offset + 1):
            required_values.append(val)
        return required_values
