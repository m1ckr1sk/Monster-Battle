"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load criterions

"""
from monster_battle.iinput import IInput


class ConsoleInput(IInput):
    """Console input.
    Allows the module to get input from the console.
    """
    def get_number_input(self, message):
        """get a number from the input """
        number = None
        while not number:
            text = input(message)
            number = self.represents_int(text)

        return number

    def represents_int(self, int_string):
        """safely convert int string to int.
        Args:
            int_string (string): integer value as string
        """
        try:
            return int(int_string)
        except ValueError:
            return None
