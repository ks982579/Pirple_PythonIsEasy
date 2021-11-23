
#myFile = open("filename","r") #r, w, a, r+
#myFile.close() # good practice

"""
File I/O
"""
cities = ["London","Paris","NYC","Cork"]
vacaFile = open("VacationCities.txt","w")
dataLen = len(cities)
dataCnt = 0
for location in cities:
   dataCnt += 1
   vacaFile.write(location)
   if dataCnt < dataLen:
      vacaFile.write("\n")
vacaFile.close()

with open("VacationCities.txt","r") as vacafile:
   for line in vacafile:
      print(line,end="")
   #end for
#end with
