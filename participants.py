"""
Participant Data
"""

parNum = 2 #Max participants
parData = []
fileName = "ParticipantData.txt"
outputfile = open(fileName,"w")

regPar = 0 #registered participants
while(regPar < parNum):
   tempPar = {} #for name, country, age
   tempPar["name"] = input("Enter name: ")
   tempPar["country"] = input("Enter origin country: ")
   tempPar["age"] = int(input("Enter you age: "))
   parData.append(tempPar)
   regPar+=1

print(parData)

for participant in parData:
   wrStr_Name = "Name: "+participant["name"]+", "
   wrStr_Cntry = "Country: "+participant["country"]+", "
   wrStr_Age = "Age: "+str(participant["age"])+"\n"
   outputfile.write(wrStr_Name)
   outputfile.write(wrStr_Cntry)
   outputfile.write(wrStr_Age)

outputfile.close()

inputFile = open(fileName, "r")

for line in inputfile:
   tempPar = 

#Closing file
inputFile.close()
