import random as r

randint = r.randint(1,10)
randArray = []
x = 0
while x < 100:
    randArray.append(r.randint(1,10))
    x += 1
#end while
print(randArray)