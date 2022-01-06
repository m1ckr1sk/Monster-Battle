# -*- coding: utf-8 -*-
"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load criteria

"""
import logging

from monster_battle.criteria.total_value_criterion import TotalValueCriterion
from monster_battle.criteria.has_item_criterion import HasItemCriterion
from monster_battle.criteria.greater_than_criterion import \
    GreaterThanCriterion
from monster_battle.criteria.odd_even_value_criterion import \
    OddEvenValueCriterion
from monster_battle.criteria.exact_match_criterion import ExactMatchCriterion
from monster_battle.criteria.bounded_match_criterion import \
    BoundedMatchCriterion
from monster_battle.evaluator import Evaluator


class Monster:
    """Monster

    This class is the main class that handles the rules logic.

    Todo:
        * Think of better way to load rules

    """

    def __init__(self, config):
        """Constructor to load the rules into the engine.
        Criteria come from a config interface and identify the monster and
        the criteria to beat the monster.
        """
        self._name = config["name"]
        self._evaluator = Evaluator()
        self._rule = config["rule"]
        self._criteria = config["criteria"]
        self._logger = logging.getLogger("root")
        self._logger.debug(
            "creating monster %s with rule %s", self._name, self._criteria
        )
        self._required_rolls = 0
        self.load_criteria(config)

    def load_criteria(self, config):
        """Load the monster config
        Args:
            config (IConfiguration): The rule configuration to load
            against.
        """
        for criterion in config["criteria"]:
            self._logger.debug(
                "criterion %s is type %s", criterion["name"], criterion["type"]
            )

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
            elif criterion["type"] == "odd even match":
                self.add_odd_even_criteria(criterion)

    def add_odd_even_criteria(self, criterion):
        """Add the odd even criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"],
            OddEvenValueCriterion(
                criterion["number_of_chances"],
                criterion["required_value"],
                criterion["is_odd"],
            ),
        )
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_bounded_match_criteria(self, criterion):
        """Add the bounded match criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"],
            BoundedMatchCriterion(
                criterion["number_of_chances"],
                criterion["required_value"],
                criterion["boundary_offset"],
            ),
        )
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_exact_match_criteria(self, criterion):
        """Add the exact match criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"],
            ExactMatchCriterion(
                criterion["number_of_chances"], criterion["required_value"]
            ),
        )
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_greater_than_value_criteria(self, criterion):
        """Add the greater than criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"],
            GreaterThanCriterion(
                criterion["number_of_chances"], criterion["required_value"]
            ),
        )
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_total_value_criteria(self, criterion):
        """Add the total value criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"],
            TotalValueCriterion(
                criterion["number_of_chances"], criterion["required_value"]
            ),
        )
        if self._required_rolls < int(criterion["number_of_chances"]):
            self._required_rolls = criterion["number_of_chances"]

    def add_has_item_criteria(self, criterion):
        """Add the has item criteria for evaluation.
        Args:
            criterion (dict): The criterion
        """
        self._evaluator.add_criteria(
            criterion["name"], HasItemCriterion(criterion["required_item"])
        )

    def battle(self, game_state, input_gatherer):
        """Battle method takes the given game state and
        runs the monster rules against the games state.
        Args:
            game_state (GameState): The state the rules should run
            against.
        """
        self._logger.debug(
            "Player has %s and has rolled %s",
            game_state.get_items(),
            game_state.get_rolls(),
        )
        self._evaluator.run_criteria(game_state, input_gatherer)
        rule = self._rule
        for criterion in self._criteria:
            self._logger.debug(
                "%s rule state is %s",
                criterion["name"],
                self._evaluator.criteria_state(criterion["name"]),
            )
            criteria_state = self._evaluator.criteria_state(criterion["name"])
            rule = rule.replace(criterion["name"], criteria_state)
        self._logger.debug("Criteria for evaluation is %s", rule)
        battle_result = eval(rule)  # pylint: disable=eval-used
        self._logger.debug("battle result with %s is %s",
                           self._name, battle_result)
        return battle_result
