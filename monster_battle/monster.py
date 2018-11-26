# -*- coding: utf-8 -*-
"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""

from monster_battle.rules.total_value_rule import TotalValueRule
from monster_battle.rules.has_item_rule import HasItemRule
from monster_battle.rules.greater_than_rule import GreaterThanRule
from monster_battle.rules.exact_match_rule import ExactMatchRule
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
        Rules come from a config interface and identify the monster and
        the conditions to beat the monster.
        """
        self._name = config["name"]
        self._evaluator = Evaluator()
        self._rule = config["rule"]
        self._conditions = config["conditions"]
        self._logger = logging.getLogger('root')
        self._logger.info("creating monster {} with rule {}".format(
            self._name, self._rule))
        self._required_rolls = 0
        self.load_config(config)

    def load_config(self, config):
        """Load config
        Args:
            config (IConfiguration): The rule configuration to load
            against.
        """
        for condition in config["conditions"]:
            self._logger.info("condition {} is type {}".format(
                condition["name"], condition["type"]))

            if condition["type"] == "item":
                self._evaluator.add_rule(
                    condition["name"],
                    HasItemRule(condition["required_item"]))
            elif condition["type"] == "total value":
                self._evaluator.add_rule(
                    condition["name"],
                    TotalValueRule(condition["number_of_chances"],
                                   condition["required_value"]))
                if self._required_rolls < int(condition["number_of_chances"]):
                    self._required_rolls = condition["number_of_chances"]
            elif condition["type"] == "greater than":
                self._evaluator.add_rule(
                    condition["name"],
                    GreaterThanRule(condition["number_of_chances"],
                                    condition["required_value"]))
                if self._required_rolls < int(condition["number_of_chances"]):
                    self._required_rolls = condition["number_of_chances"]
            elif condition["type"] == "exact match":
                self._evaluator.add_rule(
                    condition["name"],
                    ExactMatchRule(condition["number_of_chances"],
                                   condition["required_value"]))
                if self._required_rolls < int(condition["number_of_chances"]):
                    self._required_rolls = condition["number_of_chances"]

    def battle(self, game_state):
        """Battle method takes the given game state and
        runs the rules against the games state.
        Args:
            game_state (GameState): The state the rules should run
            against.
        """
        self._logger.info("Player has  {} and has rolled {}".format(
                game_state.get_items(), game_state.get_rolls()))
        self._evaluator.run_rules(game_state)
        rule = self._rule
        for condition in self._conditions:
            self._logger.info("{} rule state is {}".format(
                condition["name"],
                self._evaluator.rule_state(condition["name"])))
            rule_state = self._evaluator.rule_state(condition["name"])
            rule = rule.replace(condition["name"], rule_state)
        self._logger.info("Rule for evaulation is {}".format(rule))
        battle_result = eval(rule)
        self._logger.info("battle result with {} is {}".format(
            self._name,
            battle_result))
        return battle_result
