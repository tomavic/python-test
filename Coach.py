from Member import Member
from datetime import datetime

class Coach(Member):
  
  def __init__(self, name, expYears , signingDate, salaryPerWeek = 50000, duration = 2, bonus = 10000):
    self.__name__          = name
    self.__expYears__      = expYears
    self.__signingDate__   = signingDate
    self.__salaryPerWeek__ = salaryPerWeek
    self.__duration__      = duration
    self.__bonus__         = bonus
    
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
  
  ################# Experince Years ##############
  @property
  def ExperinceYear(self):
    return self.__expYears__
  
  @ExperinceYear.deleter
  def ExperinceYear(self):
    del self.__expYears__
  
  ############### Signing Date ###############
  @property
  def SigningDate(self):
    return self.__signingDate__
  
  @SigningDate.deleter
  def SigningDate(self):
    del self.__signingDate__
    
  ############## Salary per week #############
  @property
  def SalaryPerWeek(self):
    return self.__salaryPerWeek__
  
  @SalaryPerWeek.setter
  def SalaryPerWeek(self, value):
    if value > 200000:
      raise ValueError("Salary per week can not be more than 200000")
    else: self.__salaryPerWeek__ = value
  
  @SalaryPerWeek.deleter
  def SalaryPerWeek(self):
    del self.__salaryPerWeek__
    
  ################ Duration ###############
  @property
  def Duration(self):
    return self.__duration__
  
  @Duration.setter
  def Duration(self, value):
    if value > 3:
      raise ValueError("Contract duration can not be more than 3")
    else: self.__duration__ = value
  
  @Duration.deleter
  def Duration(self):
    del self.__duration__
    
  ############## Bonus ###############
  @property
  def Bonus(self):
    return self.__bonus__
  
  @Bonus.setter
  def Bonus(self, value):
    if value > 50000:
      raise ValueError("Bonus can not be more than 50000")
    else: self.__bonus__ = value
  
  @Bonus.deleter
  def Bonus(self):
    del self.__bonus__
    
  #################### Methods ##################
  def printPlayerData(self):
    print('My name is {} \n and my years of experince is {} and my signing date is {} and my salary per week is {} and my duration is {} and my bonus is {}'.format(self.__name__, self.__expYears__, self.__signingDate__, self.__salaryPerWeek__, self.__duration__, self.__bonus__))
    
  def calcSalaryPerYear(self):
    return self.__salaryPerWeek__ * 4 * 12 + self.__bonus__
  
  def calcRemainingDuration(self):
      return int(datetime.today().strftime("%Y")) - int(self.SigningDate)
      
  def increamentExperienceYears(self):
    self.__expYears__ +=1
    
  def addBonus(self, value):
    self.Bonus = value 