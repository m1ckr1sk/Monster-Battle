from irule import IRule

class HasItemRule(IRule):
    def __init__(self,item):
        self._item = item
        self._result = "not run"

    def execute(self, game_state):
        print "executing rule..."
        if self._item in game_state.get_items():
            print "has item rule has found required item..."
            self._result = "True"
        else:
            print "has item rule cannot find required item..."
            self._result = "False"

    def is_match(self, game_state):
        print "checking if has item rule can run..."
        return True

    def rule_state(self):
        return self._result