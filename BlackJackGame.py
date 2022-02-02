from pickle import TRUE
from random import shuffle

def createDeck():
    deck = []
    faceValues = ["A","J","Q","K"]
    for i in range(4): # 4 loops for 4 suits
        for card in range(2,11):
            deck.append(str(card))
        for card in faceValues:
            deck.append(card)
    shuffle(deck)
    shuffle(deck)
    return deck
#End createDeck() function

class Player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = 0
        self.money = money
        self.bet = 0
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

    def make_bet(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
        self.bet = 0

def printHouse(dealer: Player):
    print("House: ", end=" ")
    for card in range(len(dealer.hand)):
        if card == 0:
            print("-", end=" ")
        elif card == len(dealer.hand)-1:
            print(dealer.hand[card])
        else:
            print(dealer.hand[card], end=" ")


cardDeck = createDeck()
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]

player1 = Player()
player1.play(firstHand)
house = Player()
house.play(secondHand)

print(player1)
printHouse(house)

while True:
    action = input("Do you want another card? (y/n): ")
    action = action.lower().strip()
    if action == "y" or action == "yes":
        player1.hit(cardDeck.pop())
        print(player1)
    else:
        break
    if player1.score > 21:
        print("BUST")
        break
#End Loop
