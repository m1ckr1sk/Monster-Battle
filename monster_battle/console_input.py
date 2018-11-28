"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from monster_battle.iinput import IInput


class ConsoleInput(IInput):
    """Console input.
    Allows the module to get input from the console.
    """
    def get_number_input(self, message):
        """get a number from the input """
        number = None
        while(not number):
            text = input(message)
            number = self.represents_int(text)

        return number

    def represents_int(self, s):
        try:
            return int(s)
        except ValueError:
            return None
