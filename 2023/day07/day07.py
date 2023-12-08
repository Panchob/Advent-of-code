import sys
import os

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K','A']
TYPE_OF_HAND = ['HIGH_CARD', 'PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'FIVE_OF_A_KIND']

CARDS_PART2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K','A']

def compareHands(hand1, hand2):
  for index, card in enumerate(hand1):
    if CARDS.index(card) > CARDS.index(hand2[index]):
      return 1
    elif CARDS.index(card) < CARDS.index(hand2[index]):
      return 2

def compareHands2(hand1, hand2):
  for index, card in enumerate(hand1):
    if CARDS_PART2.index(card) > CARDS_PART2.index(hand2[index]):
      return 1
    elif CARDS_PART2.index(card) < CARDS_PART2.index(hand2[index]):
      return 2

def sortHands(hands, hasWildCard=False):
  sortedHands = [hands[0]]
  for hand in hands[1:]:
    for index, sortedHand in enumerate(sortedHands):
      
      # check if hand type is greater or lower
      if TYPE_OF_HAND.index(hand['type']) < TYPE_OF_HAND.index(sortedHand['type']):
        sortedHands.insert(index, hand)
        break
      elif TYPE_OF_HAND.index(hand['type']) == TYPE_OF_HAND.index(sortedHand['type']):
        # compare hands
        result = 0
        if hasWildCard:
          result = compareHands2(hand['hand'], sortedHand['hand'])
        else:
          result = compareHands(hand['hand'], sortedHand['hand'])
        if result == 2:
          sortedHands.insert(index, hand)
          break
        else:
          if index == len(sortedHands) - 1:
            sortedHands.append(hand)
            break
          continue
      else:
        if index == len(sortedHands) - 1:
          sortedHands.append(hand)
          break
        continue

  return sortedHands

def costHand(hands, hasWildCard=False):
  parsedHands = []
  for hand in hands:
    cards, bid = hand.split(" ")
    
    handCopy = cards

    if hasWildCard and 'J' in cards:
      # find the most common card
      cardsWithoutJ = cards.replace('J', '')
      mostCommonCard = ''
      if len(cardsWithoutJ) != 0:
        mostCommonCard = max(set(cardsWithoutJ), key=cardsWithoutJ.count)
      if mostCommonCard and cards.count(mostCommonCard) > 1:
        cards = cards.replace('J', mostCommonCard)
      # Find the most expensive card
      else:
        mappedCards = list(map(lambda x: CARDS_PART2.index(x), cards))
        mostExpensiveCard = CARDS_PART2[max(mappedCards)]
        cards = cards.replace('J', mostExpensiveCard)
      
    cardSet = set(cards)
    # Five of a kind
    if len(cardSet) == 1:
      parsedHands.append({
        'type': TYPE_OF_HAND[6],
        'bid': bid,
        'hand': handCopy,
      })
    # Four of a kind
    elif len(cardSet) == 2 and any(cards.count(card) == 4 for card in cardSet):
      parsedHands.append({
        'type': TYPE_OF_HAND[5],
        'bid': bid,
        'hand': handCopy,
      })
    # Full house
    elif len(cardSet) == 2:
      parsedHands.append({
        'type': TYPE_OF_HAND[4],
        'bid': bid,
        'hand': handCopy,
      })
    # Three of a kind
    elif len(cardSet) == 3 and any(cards.count(card) == 3 for card in cardSet):
      parsedHands.append({
        'type': TYPE_OF_HAND[3],
        'bid': bid,
        'hand': handCopy,
      })
    # Two pair
    elif len(cardSet) == 3:
      parsedHands.append({
        'type': TYPE_OF_HAND[2],
        'bid': bid,
        'hand': handCopy,
      })
    # Pair
    elif len(cardSet) == 4:
      parsedHands.append({
        'type': TYPE_OF_HAND[1],
        'bid': bid,
        'hand': handCopy,
      })
    # High card
    else:
      parsedHands.append({
        'type': TYPE_OF_HAND[0],
        'bid': bid,
        'hand': cards,
      })
  return parsedHands


def part1(hands):
  parsedHands = costHand(hands)
  sortedHands = sortHands(parsedHands)

  total = 0
  for index, hand in enumerate(sortedHands):
    total += int(hand['bid']) * (index + 1)
  print('Part 1: ' + str(total))

def part2(hands):
  parsedHands = costHand(hands, True)
  sortedHands = sortHands(parsedHands, True)

  total = 0
  for index, hand in enumerate(sortedHands):
    total += int(hand['bid']) * (index + 1)
  print('Part 2: ' + str(total))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"

  with open(os.path.join(sys.path[0], filename), "r") as f:
    hands = f.read().split("\n")
    part1(hands)
    part2(hands)
