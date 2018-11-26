import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monster_battle.rules.greater_than_rule \
    import GreaterThanRule  # noqa: E402
from monster_battle.game_state import GameState  # noqa: E402


def test_rule_not_run_returns_not_run():
    number_of_chances = 1
    required_value = 1

    test_rule = GreaterThanRule(number_of_chances, required_value)

    assert(test_rule.rule_state() == "not run")


def test_player_not_thrown_enough_is_fail():
    number_of_chances = 1
    required_value = 10

    test_rule = GreaterThanRule(number_of_chances, required_value)

    rolls = [1]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    test_rule.execute(test_game_state)
    assert(test_rule.rule_state() == "False")


def test_player_thrown_enough_is_pass():
    number_of_chances = 1
    required_value = 3

    test_rule = GreaterThanRule(number_of_chances, required_value)

    rolls = [5]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    test_rule.execute(test_game_state)

    assert(test_rule.rule_state() == "True")


def test_player_thrown_enough__over_multiple_rolls_is_pass():
    number_of_chances = 3
    required_value = 4

    test_rule = GreaterThanRule(number_of_chances, required_value)

    rolls = [1, 2, 5]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    test_rule.execute(test_game_state)

    assert(test_rule.rule_state() == "True")
