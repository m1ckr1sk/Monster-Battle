"""Monster Battle.

This module is the main monster creation module and handles the rule
logic.

Todo:
    * Think of better way to load rules

"""
from abc import ABCMeta, abstractmethod


class ICriterion:
    """Criterion interface.

    This interface must be used for all criterion.

    """
    __metaclass__ = ABCMeta

    @classmethod
    def version(cls):
        """Get the interface version """
        return "1.0"

    @abstractmethod
    def execute(self, game_state, input_gatherer):
        """Execute criterion on given game state """
        raise NotImplementedError

    @abstractmethod
    def is_match(self, game_state):
        """Can the criterion be executed """
        raise NotImplementedError

    @abstractmethod
    def criteria_state(self):
        """Get the last state of the criterion """
        raise NotImplementedError
