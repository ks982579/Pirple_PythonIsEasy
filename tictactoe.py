
print("Welcome to Tic Tac Toe!")
chc = list(range(1,10))
def drawField():
   spc = 0
   for row in range(5):
      if row%2 == 0:
         for column in range(5):
            if column%2 ==0:
               if column != 4:
                  print(chc[spc],end="")
                  spc+=1
               else:
                  print(chc[spc])
                  spc +=1
            else:
               print("|", end="")
      else:
         print("-----")

def playerMove(player):
   rtnval = False
   inputStr = "Move for {}: "
   myMove = int(input(inputStr.format(player)))
   if(myMove in chc):
      placement = chc.index(myMove)
      chc[placement] = player
   else:
      print("Incorrect value, lose a turn")
   drawField()
   winner = input("Winner (y/n): ")
   if(winner == "y"):
      rtnval = True
   return rtnval
      
gameOn = True
drawField()
while(gameOn):
   player = "X"
   chk = playerMove(player)
   if(chk):
      break
   player = "O"
   chk = playerMove(player)
   if(chk):
      break
print("Congratulations player "+player)
      
   
