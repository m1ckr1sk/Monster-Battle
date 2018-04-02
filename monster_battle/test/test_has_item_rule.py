import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from has_item_rule import HasItemRule  # noqa: E402
from game_state import GameState  # noqa: E402


def test_rule_not_run_returns_not_run():
    test_item = "test_item"

    test_rule = HasItemRule(test_item)

    assert(test_rule.rule_state() == "not run")


def test_player_not_has_item_is_fail():
    test_item = "test_item"

    test_rule = HasItemRule(test_item)

    test_items = []

    test_game_state = GameState()
    test_game_state.set_items(test_items)
    test_rule.execute(test_game_state)
    assert(test_rule.rule_state() == "False")


def test_player_has_item_is_pass():
    test_item = "test_item"

    test_rule = HasItemRule(test_item)

    test_items = []
    test_items.append(test_item)

    test_game_state = GameState()
    test_game_state.set_items(test_items)
    test_rule.execute(test_game_state)
    assert(test_rule.rule_state() == "True")
