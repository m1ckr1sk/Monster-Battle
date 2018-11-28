"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from abc import ABCMeta, abstractmethod


class IInput:
    """Input interface.

    This interface must be used for all rules.

    """
    __metaclass__ = ABCMeta

    @classmethod
    def version(cls):
        """Get the interface version """
        return "1.0"

    @abstractmethod
    def get_number_input(self, message):
        """get a number from the input """
        raise NotImplementedError
