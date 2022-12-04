import os
import sys

DRAW = {
  'A': 'X',
  'B': 'Y',
  'C': 'Z',
}

WIN = {
  'A': 'Y',
  'B': 'Z',
  'C': 'X',
}

LOSE = {
  'A': 'Z',
  'B': 'X',
  'C': 'Y',
}

def playGame(theirPlay, myPlay):
  if myPlay == DRAW[theirPlay]:
    return 3
  
  if myPlay == WIN[theirPlay]:
    return 6
  
  return 0

def findMyPlay(theirPlay, outCome):
  if outCome == 'X':
    return LOSE[theirPlay]
  if outCome == 'Y':
    return DRAW[theirPlay]
  if outCome == 'Z':
    return WIN[theirPlay]



if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    scores = {
      'X': 1,
      'Y': 2,
      'Z': 3
    }

    lines = f.read().split("\n")
    total = 0
    for line in lines:
      theirPlay, myPlay = line.split(' ')
      score = scores[myPlay]
      total += score + playGame(theirPlay, myPlay)

    print('Part 1:', total)

    total = 0
    for line in lines:
      theirPlay, outCome = line.split(' ')
      myPlay = findMyPlay(theirPlay, outCome)
      score = scores[myPlay]
      total += score + playGame(theirPlay, myPlay)
    
    print('Part 2:', total)

    
