import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monster_battle.criteria.bounded_match_criterion \
    import BoundedMatchCriterion  # noqa: E402
from monster_battle.game_state import GameState  # noqa: E402
from monster_battle.console_input import ConsoleInput  # noqa: E402


def test_criteria_not_run_returns_not_run():
    number_of_chances = 1
    required_value = 4
    boundary_offset = 4

    test_criteria = BoundedMatchCriterion(number_of_chances,
                                          required_value,
                                          boundary_offset)

    assert(test_criteria.criteria_state() == "not run")


def test_player_not_thrown_in_bounds_is_fail():
    number_of_chances = 1
    required_value = 4
    boundary_offset = 1

    test_criteria = BoundedMatchCriterion(number_of_chances,
                                          required_value,
                                          boundary_offset)

    rolls = [1]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)

    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)
    assert(test_criteria.criteria_state() == "False")


def test_player_thrown_in_bounds_pass():
    number_of_chances = 1
    required_value = 4
    boundary_offset = 1

    test_criteria = BoundedMatchCriterion(number_of_chances,
                                          required_value,
                                          boundary_offset)

    rolls = [5]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)

    assert(test_criteria.criteria_state() == "True")


def test_player_thrown_in_bounds_over_multiple_rolls_is_pass():
    number_of_chances = 3
    required_value = 4
    boundary_offset = 1

    test_criteria = BoundedMatchCriterion(number_of_chances,
                                          required_value,
                                          boundary_offset)

    rolls = [1, 2, 5]

    test_game_state = GameState()
    test_game_state.set_rolls(rolls)
    console_input = ConsoleInput()

    test_criteria.execute(test_game_state, console_input)

    assert(test_criteria.criteria_state() == "True")
