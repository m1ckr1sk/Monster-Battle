from total_value_rule import TotalValueRule
from has_item_rule import HasItemRule
from evaluator import Evaluator

class Monster():

    def __init__(self, config):
        self._name = config["name"]
        self._evaluator = Evaluator()
        self._rule = config["rule"]
        self._conditions = config["conditions"]

        print "creating monster {} with rule {}".format(self._name,self._rule)

        for condition in config["conditions"]:
            print "condition {} is type {}".format(condition["name"],condition["type"])
            if condition["type"] == "item":
                self._evaluator.add_rule(condition["name"], HasItemRule(condition["required_item"]))
            elif condition["type"] == "total value":
                self._evaluator.add_rule(condition["name"], TotalValueRule(condition["number_of_chances"],condition["required_value"]))
        
    def battle(self, game_state):
        self._evaluator.run_rules(game_state)      
        rule = self._rule
        for condition in self._conditions: 
            print "{} rule state is {}".format(condition["name"],self._evaluator.rule_state(condition["name"]))
            rule_state = self._evaluator.rule_state(condition["name"])
            rule = rule.replace(condition["name"], rule_state)
        print "Rule for evaulation is {}".format(rule)
        battle_result = eval(rule)
        print "battle result with {} is {}".format(self._name, battle_result)