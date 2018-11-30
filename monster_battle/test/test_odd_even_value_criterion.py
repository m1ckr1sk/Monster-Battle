import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monster_battle.criteria.odd_even_value_criterion \
    import OddEvenValueCriterion  # noqa: E402
from monster_battle.game_state import GameState  # noqa: E402
from monster_battle.console_input import ConsoleInput  # noqa: E402


def test_criteria_not_run_returns_not_run():
    number_of_chances = 1
    required_value = 1
    is_odd = True

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    assert(test_criteria.criteria_state() == "not run")


def test_player_not_thrown_odd_is_fail():
    number_of_chances = 1
    required_value = 1
    is_odd = True

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [2]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "False")


def test_player_not_thrown_even_is_fail():
    number_of_chances = 1
    required_value = 1
    is_odd = False

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [1]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "False")


def test_player_thrown_odd_is_pass():
    number_of_chances = 1
    required_value = 1
    is_odd = True

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [1]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "True")


def test_player_thrown_even_is_pass():
    number_of_chances = 1
    required_value = 1
    is_odd = False

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [2]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "True")


def test_player_thrown_odd_is_pass_over_multiple_throws():
    number_of_chances = 5
    required_value = 3
    is_odd = True

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [1, 4, 6, 5, 3]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "True")


def test_player_thrown_even_is_pass_over_multiple_throws():
    number_of_chances = 10
    required_value = 5
    is_odd = False

    test_criteria = OddEvenValueCriterion(
        number_of_chances, required_value, is_odd)

    rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "True")
