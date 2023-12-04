import os
import sys

def parse(line):
  [_, content] = line.split(": ")
  [myNumbers, winningNumbers] = content.split(" | ")
  myNumbers = myNumbers.strip()
  winningNumbers = winningNumbers.strip()
  myNumbers = myNumbers.split(" ")
  winningNumbers = winningNumbers.split(" ")
  # Remove empty strings
  myNumbers = list(filter(None, myNumbers))
  winningNumbers = list(filter(None, winningNumbers))
  # map strip on all elements
  myNumbers = list(map(lambda x: x.strip(), myNumbers))
  winningNumbers = list(map(lambda x: x.strip(), winningNumbers))
  # Convert to int
  myNumbers = list(map(int, myNumbers))
  winningNumbers = list(map(int, winningNumbers))

  return [myNumbers, winningNumbers]

def countMatching(myNumbers, winningNumbers):
  intersection = list(set(myNumbers) & set(winningNumbers))
  return len(intersection)

def checkWinningNumbers(myNumbers, winningNumbers):
  count = countMatching(myNumbers, winningNumbers)
  total = 0
  if count == 0:
    return total
  else:
    total = 1
    for _ in range(count - 1):
      total *= 2
    
  return total



    
def part1(card):
  lines = card.split("\n")
  total = 0
  for line in lines:
    [myNumbers, winningNumbers] = parse(line)
    total += checkWinningNumbers(myNumbers, winningNumbers)

  print('Part 1: ' + str(total))

def part2(card):
  lines = card.split("\n")
  cardCount = [1] * len(lines)
  for index in range(len(cardCount)):
    [myNumbers, winningNumbers] = parse(lines[index])
    copies = countMatching(myNumbers, winningNumbers)
    for i in range(index + 1, index + copies + 1):
      cardCount[i] += 1 * cardCount[index]
    index += 1

  print('Part 2: ' + str(sum(cardCount)))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"

  with open(os.path.join(sys.path[0], filename), "r") as f:
    card = f.read()
    part1(card)
    part2(card)