from random import shuffle

def createDeck():
    deck = []
    faceValues = ["A","J","Q","K"]
    for i in range(4): # 4 loops for 4 suits
        for card in range(2,11):
            deck.append(str(card))
        for card in faceValues:
            deck.append(card)
    return deck
cardDeck = createDeck()
shuffle(cardDeck)
shuffle(cardDeck)

class Player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = 0
        self.money = money
    def __str__(self): # allows us to call print(player)
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "Score: " + str(self.score)
        return finalStatus
    def calcScore(self): #Recalc and set score
        faceCards = {
            "A":11,
            "K":10,
            "Q":10,
            "J":10
        }
        handVal = 0
        aceCounter = 0
        for card in self.hand:
            if card == "A":
                aceCounter += 1
            try:
                handVal += faceCards[card]
            except:
                handVal += int(card)
        # if we have aces, we can lower the amount to under 21
        if handVal > 21 and aceCounter > 0:
            while aceCounter > 0:
                aceCounter -= 1
                handVal -= 10
                # Once we are under 21, we can quit the loop
                if handVal <= 21:
                    break
        return handVal

    def hit(self, card):
        self.hand.append(card)
        self.score = self.calcScore()
    # End hit() method

    def play(self, newHand):
        self.hand = newHand
        self.score = self.calcScore()
    # End play() function

    def pay(self, amount):
        self.money -= amount
    def win(self, amount):
        self.money += amount

# End All
bobby = Player(hand=[4,"A"])
bobby.hit("3")
print(bobby)
bobby.play([5,6])
print(bobby)
