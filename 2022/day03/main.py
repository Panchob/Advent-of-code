import os
import sys

def positionInAlphabet(letter):
  if letter.islower():
    return ord(letter) - 96
  else:
    return ord(letter) - 38

def getIntersection(a, b, c):
  return set(a).intersection(set(b)).intersection(set(c)).pop()

if __name__ == '__main__':
  total = 0
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().split("\n")
    for line in lines:
      firstHalf, secondHalf = [*line[:len(line) // 2]], [*line[len(line) // 2:]]
      intersection = set(firstHalf).intersection(set(secondHalf))
      for letter in intersection:
        total += positionInAlphabet(letter)
    print('Part 1:', total)
    i = 0
    total = 0
    while i < len(lines):
      badge = getIntersection(lines[i], lines[i+1], lines[i+2])
      print(badge)
      total += positionInAlphabet(badge)
      i += 3
    
    print('Part 2:', total)



  
      

