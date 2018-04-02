from game_state import GameState
from monster import Monster
from file_configuration import FileConfiguration
import json


def get_configuration():
    file_configuraiton = FileConfiguration('configurations/basic_config.json')
    configuration = file_configuraiton.get_configuration()
    return configuration

def get_player_rolls():
    player_rolls = []
    player_rolls.append(3)
    player_rolls.append(8)
    return player_rolls

def get_player_items():
    player_items = []
    player_items.append("sword")
    return player_items

def get_game_state():
    player_items = get_player_items()

    player_rolls = get_player_rolls()

    game_state = GameState()
    game_state.set_items(player_items)
    game_state.set_rolls(player_rolls)
    return game_state

try:
    
    configuration = get_configuration()
    game_state = get_game_state()

    for monster in configuration["monsters"]:
        game_monster = Monster(monster)
        game_monster.battle(game_state)
    
except Exception as exc:
    print "Should not fail " + exc.message