from monster_battle.irule import IRule
import logging


class ExactMatchRule(IRule):
    def __init__(self, number_of_chances, required_value):
        self._number_of_chances = number_of_chances
        self._required_value = required_value
        self._result = "not run"
        self._logger = logging.getLogger('root')

    def execute(self, game_state):
        self._result = "False"
        if len(game_state.get_rolls()) >= self._number_of_chances:
            self._logger.info("Exact rule requires {}".format(
                self._required_value))
            self._logger.info("Player has thrown {}".format(
                game_state.get_rolls()[:self._number_of_chances]))
            if self._required_value in \
                    game_state.get_rolls()[:self._number_of_chances]:
                        self._result = "True"

    def is_match(self, game_state):
        return len(game_state.get_rolls()) >= self._number_of_chances

    def rule_state(self):
        return self._result
