import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monster_battle.criteria.exact_match_criterion \
    import ExactMatchCriterion  # noqa: E402
from monster_battle.game_state import GameState  # noqa: E402
from monster_battle.console_input import ConsoleInput  # noqa: E402


def test_criteria_not_run_returns_not_run():
    number_of_chances = 1
    required_value = 1

    test_criteria = ExactMatchCriterion(number_of_chances, required_value)

    assert(test_criteria.criteria_state() == "not run")


def test_player_not_thrown_exact_is_fail():
    number_of_chances = 1
    required_value = 4

    test_criteria = ExactMatchCriterion(number_of_chances, required_value)

    rolls = [5]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "False")


def test_player_thrown_exact_is_pass():
    number_of_chances = 1
    required_value = 3

    test_criteria = ExactMatchCriterion(number_of_chances, required_value)

    rolls = [3]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)

    assert(test_criteria.criteria_state() == "True")


def test_player_thrown_exact_over_multiple_rolls_is_pass():
    number_of_chances = 3
    required_value = 4

    test_criteria = ExactMatchCriterion(number_of_chances, required_value)

    rolls = [1, 2, 4]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)

    assert(test_criteria.criteria_state() == "True")
