from abc import ABC, abstractmethod

class Member(ABC):
  
  @abstractmethod
  def printPlayerData(self):
    pass
  
  @abstractmethod
  def calcSalaryPerYear(self):
    pass
  
  @abstractmethod
  def calcRemainingDuration(self):
    pass
