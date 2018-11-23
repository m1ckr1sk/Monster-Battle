"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from monster_battle.irule import IRule

class HasItemRule(IRule):
    """Has item rule.
    This rule allows a config to test if the player has s specified
    item.
    """
    def __init__(self, item):
        self._item = item
        self._result = "not run"

    def execute(self, game_state):
        """Execute the rule.
        Args:
            game_state (GameState): The game state to assess
        """
        print("executing rule...")
        if self._item in game_state.get_items():
            print("has item rule has found required item...")
            self._result = "True"
        else:
            print("has item rule cannot find required item...")
            self._result = "False"

    def is_match(self, game_state):
        """Can the rule run?.
        Args:
            game_state (GameState): The game state to assess
        """
        print("checking if has item rule can run...")
        return True

    def rule_state(self):
        """Get the last state of the rule"""
        return self._result
