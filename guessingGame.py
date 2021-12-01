from random import randint

myRange = [1,100]
myVal = randint(1,100)
gameOn = True
counter = 0
while(gameOn):
    urGuess = input("Please enter guess between 1 & 100: ")
    counter += 1
    urGuess = int(urGuess)
    if urGuess == myVal:
        break
    elif urGuess < myVal:
        print("Too low")
    else:
        print("Too high")
print("You guessed correctly in {} tries!".format(counter))