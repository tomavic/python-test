from abc import ABC


class Member(ABC):
    def __init__(self, name):
      self.__name__ = name
    
    @property
    def Name(self):
      return self.__name__
    
    @Name.setter
    def Name(self, value):
      self.__name__ = value
    
    @Name.deleter
    def Name(self):
      del self.__name__
