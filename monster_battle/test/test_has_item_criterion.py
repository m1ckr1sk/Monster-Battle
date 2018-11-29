import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monster_battle.criteria.has_item_criterion \
    import HasItemCriterion  # noqa: E402
from monster_battle.game_state import GameState  # noqa: E402
from monster_battle.console_input import ConsoleInput  # noqa: E402


def test_criteria_not_run_returns_not_run():
    test_item = "test_item"

    test_criteria = HasItemCriterion(test_item)

    assert(test_criteria.criteria_state() == "not run")


def test_player_not_has_item_is_fail():
    test_item = "test_item"

    test_criteria = HasItemCriterion(test_item)

    test_items = []

    test_game_state = GameState()
    test_game_state.set_items(test_items)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "False")


def test_player_has_item_is_pass():
    test_item = "test_item"

    test_criteria = HasItemCriterion(test_item)

    test_items = []
    test_items.append(test_item)

    test_game_state = GameState()
    test_game_state.set_items(test_items)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "True")
