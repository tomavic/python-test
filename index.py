from abc import ABC, abstractmethod
import datetime

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

##########################################

class Player(Member):
  
  def __init__(self, name, playerNumber, signingDate, salaryPerWeek = 20000, contractDuration = 3, playedMatchesNumber = 0):

    dateInYeaar = datetime.datetime(signingDate, 1, 1)
    
    self.__name__                = name
    self.__playerNumber__        = playerNumber
    self.__signingDate__         = dateInYeaar.strftime("%Y")
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
      raise ValueError("Name cannot exceed 20 characters.")
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
    self.__salaryPerWeek__ = value
  
  @SalaryPerWeek.deleter
  def SalaryPerWeek(self):
    del self.__salaryPerWeek__
    
  ############### CONTRACT DURATION ################
  @property
  def ContractDuration(self):
    return self.__contractDuration__
  
  @ContractDuration.setter
  def ContractDuration(self, value):
    self.__contractDuration__ = value
  
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
    print('This is remaining duration data')
  
  def IncreamentMatches(self):
    self.__playedMatchesNumber__ +=1
    
  def increamentContractDutarion(self, years):
    self.__signingDate__ = self.__signingDate__ + years

##############################

class Captin(Player):
  
  def __init__(self, name, playerNumber, signingDate, leadingMatches = 10, bonus = 5000):
    super().__init__(name, playerNumber, signingDate)
    self.__leadingMatches__ = leadingMatches
    self.__bonus__ = bonus

  ############### LEADING MATCHES ################
  def getLeadingMatchesNumber(self):
    return self.__leadingMatches__
  
  def setLeadingMatchesNumber(self, value):
    self.__leadingMatches__ = value
  
  def delLeadingMatchesNumber(self):
    del self.__leadingMatches__
    
  LeadingMatchesNumber = property(getLeadingMatchesNumber, setLeadingMatchesNumber, delLeadingMatchesNumber)   
  
  ############### BONUS ################
  def getBonus(self):
    return self.__bonus__
  
  def setBonus(self, value):
    self.__bonus__ = value
  
  def delBonus(self):
    del self.__bonus__
    
  Bonus = property(getBonus, setBonus, delBonus)   
      

  def printPlayerData(self):
    print('My name is {} and my number is {} and my signing date is {} and my leading matches number is {} and my bonus is {}'.format(self.__name__, self.__playerNumber__, self.__signingDate__, self.__leadingMatches__, self.__bonus__))

  def calcSalaryPerYear(self):
      return super().calcSalaryPerYear() + self.__bonus__

  def increamentLeadingMtaches(self):
    self.__leadingMatches__ +=1

###############################################

class Coach(Member):
  
  def __init__(self, name, expYears , signingDate, salaryPerWeek = 50000, duration = 2, bonus = 10000):
    self.__name__          = name
    self.__expYears__      = expYears
    self.__signingDate__   = signingDate
    self.__salaryPerWeek__ = salaryPerWeek
    self.__duration__      = duration
    self.__bonus__         = bonus
    
  ############### NAME ################
  def getName(self):
    return self.__name__
  
  def setName(self, value):
    self.__name__ = value
  
  def delName(self):
    del self.__name__
    
  name = property(getName, setName, delName) 
  
  ################# Experince Years ##############
  def getExperinceYear(self):
    return self.__expYears__
  
  def setExperinceYear(self, value):
    self.__expYears__ = value
  
  def delExperinceYear(self):
    del self.__expYears__
    
  ExperinceYear = property(getExperinceYear, setExperinceYear, delExperinceYear) 
  
  ############### Signing Date ###############
  def getSigningDate(self):
    return self.__signingDate__
  
  def setSigningDate(self, value):
    self.__signingDate__ = value
  
  def delSigningDate(self):
    del self.__signingDate__
    
  SigningDate = property(getSigningDate, setSigningDate, delSigningDate) 
  
  ############## Salary per week #############
  def getSalaryPerWeek(self):
    return self.__salaryPerWeek__
  
  def setSalaryPerWeek(self, value):
    self.__salaryPerWeek__ = value
  
  def delSalaryPerWeek(self):
    del self.__salaryPerWeek__
    
  SalaryPerWeek = property(getSalaryPerWeek, setSalaryPerWeek, delSalaryPerWeek) 
    
  ################ Duration ###############
  def getDuration(self):
    return self.__duration__
  
  def setDuration(self, value):
    self.__duration__ = value
  
  def delDuration(self):
    del self.__duration__
    
  Duration = property(getDuration, setDuration, delDuration)   
  
  ############## Bonus ###############
  def getBonus(self):
    return self.__bonus__
  
  def setBonus(self, value):
    self.__bonus__ = value
  
  def delBonus(self):
    del self.__bonus__
    
  Bonus = property(getBonus, setBonus, delBonus)   
  
  #################### Methods ##################
  def printPlayerData(self):
    print('My name is {} \n and my years of experince is {} and my signing date is {} and my salary per week is {} and my duration is {} and my bonus is {}'.format(self.__name__, self.__expYears__, self.__signingDate__, self.__salaryPerWeek__, self.__duration__, self.__bonus__))
    
  def calcSalaryPerYear(self):
    return self.__salaryPerWeek__ * 4 * 12 + self.__bonus__
  
  def calcRemainingDuration(self):
      self.__duration__ +=1
      
  def increamentExperienceYears(self):
    self.__expYears__ +=1
    
##################################
    

hooka = Player()

hooka.Name = 'Carlo'
hooka.PlayerNumber = 10
hooka.
print(hooka.PlayerNumber)

############################
