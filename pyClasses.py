"""
Classes
"""
class Team:
   """
   This is some information about the Team Class
   """
   def __init__(self,teamName: str="none", location: str="Earth"):
      self.teamName = teamName
      self.teamOrigin = location
   def displayInfo(self):
      mssg = "Team Name: {}"
      print(mssg.format(self.teamName))
      mssg = "Team Origin: {}"
      print(mssg.format(self.teamOrigin))

class Player(Team):
   def __init__(self,aTeam:object,aName:str):
      Team.__init__(self,aTeam.teamName,aTeam.teamOrigin)
      self.playerName = aName
      self.PlayerPoints = 0
   def ScoredPoint(self):
      self.PlayerPoints += 1
   def setName(self,pName:str):
      self.PlayerName = pName
   #def __str__

HellHounds = Team("HellHounds","Cork, Ireland")
HellHounds.displayInfo()

Tom = Player(HellHounds,"Tom")
print(Tom.playerName)
