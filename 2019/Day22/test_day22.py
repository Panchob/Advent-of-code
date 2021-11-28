import unittest
from day22 import *

class TestsShuffle(unittest.TestCase):
    
    def testdealIntoNewStack(self):
        deck = Deck(10)
        deck.dealIntoNewStack()
        self.assertEqual(deck.cards(), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    
    def testCutNCards(self):
        deck = Deck(10)
        deck.cut(3)
        self.assertEqual(deck.cards(), [3, 4, 5, 6, 7, 8, 9, 0, 1, 2])

    def testCutNCardsNegative(self):
        deck = Deck(10)
        deck.cut(-4)
        self.assertEqual(deck.cards(), [6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
    
    def testDealWithIncrement(self):
        deck = Deck(10)
        deck.dealWithIncrement(3)
        self.assertEqual(deck.cards(), [0, 7, 4, 1, 8, 5, 2, 9, 6, 3])
    
    def testShuffle1(self):
        deck = Deck(10)
        deck.dealWithIncrement(7)
        deck.dealIntoNewStack()
        deck.dealIntoNewStack()
        self.assertEqual(deck.cards(), [0, 3, 6, 9, 2, 5, 8, 1, 4, 7])
    
    def testShuffle2(self):
        deck = Deck(10)
        deck.cut(6)
        deck.dealWithIncrement(7)
        deck.dealIntoNewStack()
        self.assertEqual(deck.cards(), [3, 0, 7, 4, 1, 8, 5, 2, 9, 6])

    def testShuffle3(self):
        deck = Deck(10)
        deck.dealWithIncrement(7)
        deck.dealWithIncrement(9)
        deck.cut(-2)
        self.assertEqual(deck.cards(), [6, 3, 0, 7, 4, 1, 8, 5, 2, 9])
    
    def testShuffle4(self):
        deck = Deck(10)
        deck.dealIntoNewStack()
        deck.cut(-2)
        deck.dealWithIncrement(7)
        deck.cut(8)
        deck.cut(-4)
        deck.dealWithIncrement(7)
        deck.cut(3)
        deck.dealWithIncrement(9)
        deck.dealWithIncrement(3)
        deck.cut(-1)
        self.assertEqual(deck.cards(), [9, 2, 5, 8, 1, 4, 7, 0, 3, 6])

        

if __name__ == '__main__': 
    unittest.main() 