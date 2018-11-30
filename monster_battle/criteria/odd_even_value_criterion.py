"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
import logging
from monster_battle.criteria.icriterion import ICriterion


class OddEvenValueCriterion(ICriterion):
    """Odd or Even value criterion.
    This rule passes if the value is either odd or even depending
    on the required value. The number required is hown many odd/even
    numbers are required and the number of chances is the rolls that
    can be thrown to meet the number required.
    """

    def __init__(self, number_of_chances, required_value, isodd):
        self._number_of_chances = number_of_chances
        self._required_value = required_value
        self._isodd = isodd
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

            self._logger.info("odd is %s",
                              self._isodd)
            self._logger.info("need to find at least %s in %s..",
                              self._required_value,
                              sum(game_state.get_rolls()
                                  [:self._number_of_chances]))
            number_of_odd_numbers = self.count_odd_numbers_in_rolls(
                game_state.get_rolls()[:self._number_of_chances])
            if(self._isodd):
                self._result = str(required_value <= number_of_odd_numbers)
            else:
                self._result = str(required_value <=
                                   (self._number_of_chances -
                                    number_of_odd_numbers))

    def count_odd_numbers_in_rolls(self, rolls):
        if not rolls:
            return 0
        return rolls[0] % 2 + self.count_odd_numbers_in_rolls(rolls[1:])

    def is_match(self, game_state):
        """Can the rule run?.
        Args:
            game_state (GameState): The game state to assess
        """
        return len(game_state.get_rolls()) >= self._number_of_chances

    def criteria_state(self):
        """Get the last state of the criterion"""
        return self._result
