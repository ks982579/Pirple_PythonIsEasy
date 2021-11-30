import random as r
import time

startTime = time.perf_counter()

#from random import randint as rInt
randArray = []
x = 0
while x < 1000:
    randArray.append(r.randint(1,10))
    x += 1
#end while
#print(r.choice(randArray))
endTime = time.perf_counter()
print(endTime-startTime)
print(1/60)