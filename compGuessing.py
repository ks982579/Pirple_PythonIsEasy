from random import random
from time import perf_counter as clock
randVal = random()

gameOn = True
bounds = {
    "upper": 1.0,
    "lower": 0.0
}
counter = 0
startTime = clock()
while(gameOn):
    guess = (bounds["upper"] + bounds["lower"])/2
    counter += 1
    if guess == randVal:
        break
    elif guess < randVal:
        bounds["lower"] = guess
    else:
        bounds["upper"] = guess
endTime = clock()
elapTime = round(endTime - startTime,8)
print("Guessed correctly in {} guesses!".format(counter))
print("{} seconds".format(elapTime))
# by Kevin Sullivan