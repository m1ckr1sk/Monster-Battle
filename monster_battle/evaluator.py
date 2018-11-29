"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from monster_battle.criteria.icriterion import ICriterion


class Evaluator():
    """Evaluator.

    This class runs rules and reports on the state of the rule.

    """

    def __init__(self):
        self._criterias = {}

    def add_criteria(self, rule_id, rule):
        """Add rule to the list of rules to run.
        Args:
            rule_id (int): Criteria id
            rule (Riule): Criteria
        """
        if not isinstance(rule, ICriterion):
            raise Exception('Bad interface')
        if ICriterion.version() != '1.0':
            raise Exception('Bad revision')

        self._criterias[rule_id] = rule

    def run_criterias(self, game_state, input_gatherer):
        """Run rules on a given game state
        Args:
            game_state (game_state): game state to assess
        """
        for rule_id in self._criterias:
            if self._criterias[rule_id].is_match(game_state):
                self._criterias[rule_id].execute(game_state, input_gatherer)

    def criteria_state(self, rule_id):
        """Get the state of a given rule based on the last time it ran
        Args:
            rule_id (int): rule id
        """
        return self._criterias[rule_id].criteria_state()
