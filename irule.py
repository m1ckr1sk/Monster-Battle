from abc import ABCMeta, abstractmethod

class IRule:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"
    @abstractmethod
    def execute(self, game_state): raise NotImplementedError
    @abstractmethod
    def is_match(self): raise NotImplementedError
    @abstractmethod
    def rule_state(self): raise NotImplementedError