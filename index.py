from Member import Member
from Player import Player
from Captin import Captin, Player
from Coach import Coach
from Team import Team


# 1- create coach object
Guardiola = Coach('Pep', 12, 2012)

# 2- create team object
Blograna = Team("Barcelona", 2, 2010)

# 3- add four players
Blograna.addPlayer("Zidane",5,20000,2003,3,12) 
Blograna.addPlayer("Henry", 14, 23000, 2004, 4, 8)
Blograna.addPlayer("Messi", 10, 50000, 2007, 5, 7)
Blograna.addPlayer("Iniesta", 8, 26000, 2006, 6, 6)

# 4- print number of players
print(Blograna.__len__())

# 5- print team captin data
Blograna.printCaptainInfo()

# 6- print whole team data
Blograna.printTeamData()

# 7- calc all salaries
Blograna.calcAllSalary()

# 8- search player
Blograna.searchPlayer(8)

# 9- search player using indexer

# 10- delete one of the players
Blograna.deletePlayer(7)

# 11- print captin info
Blograna.printCaptainInfo()

# 12- print whole team data
Blograna.printTeamData()

# 13- print number of players
print(Blograna.__len__())

# 14- print all team salary 
Blograna.calcAllSalary()
