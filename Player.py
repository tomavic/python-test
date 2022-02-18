from Member import Member
from datetime import datetime
class Player(Member):
  
  def __init__(self, name, playerNumber, signingDate, salaryPerWeek = 20000, contractDuration = 3, playedMatchesNumber = 0):

    self.__name__                = name
    self.__playerNumber__        = playerNumber
    self.__signingDate__         = datetime(signingDate, 1, 1).strftime("%Y")
    self.__salaryPerWeek__       = salaryPerWeek
    self.__contractDuration__    = contractDuration
    self.__playedMatchesNumber__ = playedMatchesNumber
  
  
  ############### NAME ################
  @property
  def Name(self):
    return self.__name__
  
  @Name.setter
  def Name(self, value):
    self.__name__ = value
  
  @Name.deleter
  def Name(self):
    del self.__name__
    
  ############### PLAYER NAME ################
  
  @property
  def PlayerNumber(self):
    return self.__playerNumber__;
  
  @PlayerNumber.setter
  def PlayerNumber(self, value):
    if value > 30:
      raise ValueError("Player number can not be more than 30")
    else: self.__playerNumber__ = value
  
  @PlayerNumber.deleter
  def PlayerNumber(self):
    del self.__playerNumber__
    
  ############### SIGNING DATE ################
  
  @property
  def SigningDate(self):
    return self.__signingDate__;
  
  @SigningDate.deleter
  def SigningDate(self):
    del self.__signingDate__
    
  ############### SALARY PER WEEk ################
  @property
  def SalaryPerWeek(self):
    return self.__salaryPerWeek__
  
  @SalaryPerWeek.setter
  def SalaryPerWeek(self, value):
    if value > 100000:
      raise ValueError("Salary Per Week can not be more than 100,000")
    else: self.__salaryPerWeek__ = value
  
  @SalaryPerWeek.deleter
  def SalaryPerWeek(self):
    del self.__salaryPerWeek__
    
  ############### CONTRACT DURATION ################
  @property
  def ContractDuration(self):
    return self.__contractDuration__
  
  @ContractDuration.setter
  def ContractDuration(self, value):
    if value > 5:
      raise ValueError("Max contract duration is five years")
    else: self.__contractDuration__ = value
  
  @ContractDuration.deleter
  def ContractDuration(self):
    del self.__contractDuration__
    
  ############### PLAYED MATCHES ################
  
  @property
  def PlayedMatchesNumber(self):
    return self.__playedMatchesNumber__
  
  @PlayedMatchesNumber.setter
  def PlayedMatchesNumber(self, value):
    self.__playedMatchesNumber__ = value
  
  @PlayedMatchesNumber.deleter
  def PlayedMatchesNumber(self):
    del self.__playedMatchesNumber__
    
  ############### METHODS ##################
  def printPlayerData(self):
    print('My name is {} and my number is {} and my signing date is {}'.format(self.__name__, self.__playerNumber__, self.__signingDate__))
    
  def calcSalaryPerYear(self):
    return self.__salaryPerWeek__ * 4 * 12
  
  def calcRemainingDuration(self):
    return int(datetime.today().strftime("%Y")) - int(self.SigningDate)
  
  def IncreamentMatches(self):
    self.__playedMatchesNumber__ +=1
    
  def increamentContractDutarion(self, years):
    self.__signingDate__ = self.__signingDate__ + years
