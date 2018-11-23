from monster_battle.irule import IRule
from monster_battle.greater_than_rule import GreaterThanRule

class Evaluator(object):

    def __init__(self):
        self._rules = {}

    def add_rule(self, rule_id, rule):
        if not isinstance(rule, IRule): raise Exception('Bad interface')
        if not IRule.version() == '1.0': raise Exception('Bad revision')

        self._rules[rule_id] = rule

    def run_rules(self, game_state):
        for rule_id in self._rules:
            if self._rules[rule_id].is_match(game_state):
                self._rules[rule_id].execute(game_state)

    def rule_state(self, rule_id):
        return self._rules[rule_id].rule_state()
            
