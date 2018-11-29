# -*- coding: utf-8 -*-
"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""

from monster_battle.criteria.total_value_criterion import TotalValueCriterion
from monster_battle.criteria.has_item_criterion import HasItemCriterion
from monster_battle.criteria.greater_than_criterion import GreaterThanCriterion
from monster_battle.criteria.exact_match_criterion import ExactMatchCriterion
from monster_battle.criteria.bounded_match_criterion \
    import BoundedMatchCriterion
from monster_battle.evaluator import Evaluator
import logging


class Monster():
    """Monster

    This class is the main class that handles the rules logic.

    Todo:
        * Think of better way to load rules

    """

    def __init__(self, config):
        """Constructor to load the rules into the engine.
        Criterias come from a config interface and identify the monster and
        the criteria to beat the monster.
        """
        self._name = config["name"]
        self._evaluator = Evaluator()
        self._rule = config["rule"]
        self._criteria = config["criteria"]
        self._logger = logging.getLogger('root')
        self._logger.info("creating monster {} with rule {}".format(
            self._name, self._criteria))
        self._required_rolls = 0
        self.load_criteria(config)

    def load_criteria(self, config):
        """Load the monster config
        Args:
            config (IConfiguration): The rule configuration to load
            against.
        """
        for criterion in config["criteria"]:
            self._logger.info("criterion {} is type {}".format(
                criterion["name"], criterion["type"]))

            if criterion["type"] == "item":
                self.add_has_item_criteria(criterion)
            elif criterion["type"] == "total value":
                self.add_total_value_criteria(criterion)
            elif criterion["type"] == "greater than":
                self.add_greater_than_value_criteria(criterion)
            elif criterion["type"] == "exact match":
                self.add_exact_match_criteria(criterion)
            elif criterion["type"] == "bounded match":
                self.add_bounded_match_criteria(criterion)

    def add_bounded_match_criteria(self, criterion):
        self._evaluator.add_criteria(
            criterion["name"],
            BoundedMatchCriterion(criterion["number_of_chances"],
                                  criterion["required_value"],
                                  criterion["boundary_offset"]))
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_exact_match_criteria(self, criterion):
        self._evaluator.add_criteria(
            criterion["name"],
            ExactMatchCriterion(criterion["number_of_chances"],
                                criterion["required_value"]))
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_greater_than_value_criteria(self, criterion):
        self._evaluator.add_criteria(
            criterion["name"],
            GreaterThanCriterion(criterion["number_of_chances"],
                                 criterion["required_value"]))
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_total_value_criteria(self, criterion):
        self._evaluator.add_criteria(
            criterion["name"],
            TotalValueCriterion(criterion["number_of_chances"],
                                criterion["required_value"]))
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_has_item_criteria(self, criterion):
        self._evaluator.add_criteria(
            criterion["name"],
            HasItemCriterion(criterion["required_item"]))

    def battle(self, game_state, input_gatherer):
        """Battle method takes the given game state and
        runs the monster rules against the games state.
        Args:
            game_state (GameState): The state the rules should run
            against.
        """
        self._logger.info("Player has  {} and has rolled {}".format(
            game_state.get_items(), game_state.get_rolls()))
        self._evaluator.run_criterias(game_state, input_gatherer)
        rule = self._rule
        for criterion in self._criteria:
            self._logger.info("{} rule state is {}".format(
                criterion["name"],
                self._evaluator.criteria_state(criterion["name"])))
            criteria_state = self._evaluator.criteria_state(criterion["name"])
            rule = rule.replace(criterion["name"], criteria_state)
        self._logger.info("Criteria for evaulation is {}".format(rule))
        battle_result = eval(rule)
        self._logger.info("battle result with {} is {}".format(
            self._name,
            battle_result))
        return battle_result
