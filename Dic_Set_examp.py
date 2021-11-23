"""
Dictionaries and Sets Example
"""

BlackShoes = {
    #Shoe Size : Number in Inventory
    38:0, 39:1, 40:4, 40:3, 42:2, 43:3, 44:1
    }
print("Welcome...")
print(BlackShoes)
while(True):
    purchaseSize = int(input("Shoe Size: "))
    if BlackShoes[purchaseSize] >0:
        BlackShoes[purchaseSize] -= 1
    else:
        print("Size is out of stock")
    print(BlackShoes)
