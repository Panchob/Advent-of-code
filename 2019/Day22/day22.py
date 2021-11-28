import os
import sys

class Deck:
    def __init__(self, nbOfCards):
        self.deck = list(range(0, nbOfCards))

    def dealIntoNewStack(self):
        self.deck.reverse()
    

    # Takes positive and negative input
    def cut(self, nbToCut):
        cut = self.deck[ :nbToCut]
        newDeck = self.deck[nbToCut:: ]
        self.deck = newDeck + cut
    

    def dealWithIncrement(self, increment):
        deckSize = len(self.deck)
        dealt = [None] * deckSize
        i = 0

        while self.deck:
            if dealt[i] is None:
                dealt[i] = self.topCard()
            i += increment

            if i > deckSize:
                i = i - deckSize
        
        self.deck = dealt

    def topCard(self):
        return self.deck.pop(0)

    def cards(self):
        return self.deck

def executeCommand(line, deck):
    neg = "-" if "-" in line else "" 
    num = neg + "".join(i for i in line if i.isdigit())

    if "cut" in line:
        deck.cut(int(num))
    elif "increment" in line:
        deck.dealWithIncrement(int(num))
    else:
        deck.dealIntoNewStack()

def PartOne():
    deck = Deck(10007)

    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        for line in f.readlines():
            executeCommand(line, deck)
        
    print("PART ONE: The card #2019 is at position:", deck.cards().index(2019))


if __name__ == "__main__":
    PartOne()
    # TODO: part 2?





    






     