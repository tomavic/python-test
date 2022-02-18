from Player import Player


class Team():
  
  def __init__(self, name, position, coach, players = [], captin= None, playersNumber=0):
    self.__name__ = name
    self.__position__ = position
    self.__coach__ = coach
    self.__players__ = []
    self.__captin__ = captin
    self.__playersNumber__ = playersNumber
  
  @property
  def Name(self):
    return self.__name__
  
  @Name.setter
  def Name(self, value):
    self.__name__ = value
  
  @Name.deleter
  def Name(self):
    del self.__name__
  
  ######################
  @property
  def Position(self):
    return self.__position__
  
  @Position.setter
  def Position(self, value):
    self.__position__ = value
  
  @Position.deleter
  def Position(self):
    del self.__position__
    
  #####################
  
  @property
  def coach(self):
    return self.__coach__
  
  @coach.setter
  def coach(self, value):
    self.__coach__ = value
  
  @coach.deleter
  def coach(self):
    del self.__coach__
  
  #####################
  
  @property
  def players(self):
    return self.__players__
  
  @players.setter
  def players(self, value):
    self.__players__ = value
  
  @players.deleter
  def players(self):
    del self.__players__
    
###########################
  @property
  def captin(self):
    return self.__captin__
  
  @captin.setter
  def captin(self, value):
    self.__captin__ = value
    
  @captin.deleter
  def captin(self):
    del self.__captin__
    
  #######################
  
  @property
  def playersNumber(self): 
    return self.__playersNumber__
  
  @playersNumber.setter
  def playersNumber(self, value):
    self.__playersNumber__ = value
    
  @playersNumber.deleter
  def playersNumber(self):
    del self.__playersNumber__
    
  #####################
  
  def printTeamData(self):
    print('My team is {} \n and my position in league is {} and my coach is {} and my players are {} and my captin is {} and my players number is {}'.format(self.Name, self.Position, self.coach, self.players, self.captin, self.playersNumber))
  
  
  def printCaptainInfo(self):
    # self.captin.printPlayerData()
    print("captin printPlayerData")
    
  def addPlayer(self, name, number, salaryPerWeek, signingDate, contractDuration, matchesPlayed):
    for x in self.players:
      if x.PlayerNumber == number:
        print("change the player number")
        return
    player = Player(name, number, signingDate, salaryPerWeek, contractDuration, matchesPlayed)
    self.__players__.append(player)
    self.playersNumber +=1
    # self.modifyCaptin()
      
  def modifyCaptin(self, bonus, matchesNumber):
    # todo excract player with highest played matches
    self.captin.Bonus = bonus
    
  def deletePlayer(self, pNumber):
    for player in self.players:
      if player.PlayerNumber == pNumber:
        self.players.remove(player)
        self.playersNumber -=1
        return
      else: 
        print("No player exists with this number")
        
  def searchPlayer(self, pNumber):
    for player in self.players:
      if player.PlayerNumber == pNumber:
        player.printPlayerData()
        return
        
  def calcAllSalary(self):
    # todo should calculate all salaries
    print("All Salaries")
    
  def __len__(self):
    return self.playersNumber