from abc import ABCMeta, abstractmethod


class IConfiguration:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def get_configuration(self): raise NotImplementedError
