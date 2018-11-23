from monster_battle.game_state import GameState
from monster_battle.monster import Monster
from monster_battle.file_configuration import FileConfiguration


def get_configuration():
    file_configuraiton = FileConfiguration('monster_battle/configurations/basic_config.json')
    configuration = file_configuraiton.get_configuration()
    return configuration


def get_player_rolls():
    player_rolls = []
    player_rolls.append(3)
    player_rolls.append(8)
    player_rolls.append(4)
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
    print ("Should not fail " + exc.message)
