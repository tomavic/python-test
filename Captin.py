from Player import Player

class Captin(Player):
  
  def __init__(self, name, playerNumber, signingDate, leadingMatches = 10, bonus = 5000):
    super().__init__(name, playerNumber, signingDate)
    self.__leadingMatches__ = leadingMatches
    self.__bonus__ = bonus

  ############### LEADING MATCHES ################
  @property
  def LeadingMatchesNumber(self):
    return self.__leadingMatches__
  
  @LeadingMatchesNumber.deleter
  def LeadingMatchesNumber(self):
    del self.__leadingMatches__
  
  ############### BONUS ################
  
  @property
  def Bonus(self):
    return self.__bonus__
  
  @Bonus.setter
  def Bonus(self, value):
    if value > 100000:
      raise ValueError("Bonus can not be more than 100,000")
    else: self.__bonus__ = value
  
  @Bonus.deleter
  def Bonus(self):
    del self.__bonus__

  def printPlayerData(self):
    print('My name is {} and my number is {} and my signing date is {} and my leading matches number is {} and my bonus is {}'.format(self.__name__, self.__playerNumber__, self.__signingDate__, self.__leadingMatches__, self.__bonus__))

  def calcSalaryPerYear(self):
      return super().calcSalaryPerYear() + self.__bonus__

  def increamentLeadingMtaches(self):
    self.__leadingMatches__ +=1
