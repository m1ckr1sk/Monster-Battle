from monster_battle.game_state import GameState
from monster_battle.monster import Monster
from monster_battle.configuration.file_configuration import FileConfiguration
import logging
import random


def get_configuration():
    file_configuraiton = FileConfiguration(
        'monster_battle/configuration_files/basic_config.json')
    configuration = file_configuraiton.get_configuration()
    return configuration


def get_player_rolls(number_of_rolls):
    player_rolls = []
    for _ in range(number_of_rolls):
        player_rolls.append(random.randint(1, 6))
    return player_rolls


def get_player_items():
    player_items = []
    player_items.append("sword")
    return player_items


def generate_game_state(number_of_rolls):
    player_items = get_player_items()

    player_rolls = get_player_rolls(number_of_rolls)

    game_state = GameState()
    game_state.set_items(player_items)
    game_state.set_rolls(player_rolls)
    return game_state


logger = logging.getLogger('root')
try:

    configuration = get_configuration()

    for monster in configuration["monsters"]:
        game_monster = Monster(monster)
        game_state = generate_game_state(game_monster._required_rolls)
        game_monster.battle(game_state)

except Exception as exc:
    print("Should not fail " + str(exc))
