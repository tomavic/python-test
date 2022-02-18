from Member import Member
from Player import Player
from Captin import Captin, Player
from Coach import Coach
from Team import Team


Guardiola = Coach('Pep', 12, 2012)

Messi = Captin("El PaPa", 10, 2008)

Gunners = Team("Ronalldo", 2, 2010, [], Messi)

print(Gunners.printCaptainInfo())


