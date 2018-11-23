"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from monster_battle.irule import IRule


class Evaluator():
    """Evaluator.

    This class runs rules and reports on the state of the rule.

    """

    def __init__(self):
        self._rules = {}

    def add_rule(self, rule_id, rule):
        """Add rule to the list of rules to run.
        Args:
            rule_id (int): Rule id
            rule (Riule): Rule
        """
        if not isinstance(rule, IRule):
            raise Exception('Bad interface')
        if IRule.version() != '1.0':
            raise Exception('Bad revision')

        self._rules[rule_id] = rule

    def run_rules(self, game_state):
        """Run rules on a given game state
        Args:
            game_state (game_state): game state to assess
        """
        for rule_id in self._rules:
            if self._rules[rule_id].is_match(game_state):
                self._rules[rule_id].execute(game_state)

    def rule_state(self, rule_id):
        """Get the state of a given rule based on the last time it ran
        Args:
            rule_id (int): rule id
        """
        return self._rules[rule_id].rule_state()
