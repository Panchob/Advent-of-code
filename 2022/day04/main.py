import os
import sys

def isOverlapping(s1, e1, s2, e2):
  set1 = set(range(s1, e1 + 1))
  set2 = set(range(s2, e2 + 1))
  return len(set1.intersection(set2)) > 0

if __name__ == '__main__':
  part1 = 0
  part2 = 0
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    total = 0
    for line in lines:
      zone1, zone2 = line.split(',')
      s1, e1 = map(int, zone1.split('-'))
      s2, e2 = map(int, zone2.split('-'))

      if (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2):
        part1 += 1
        # Already overlapping
        part2 += 1
      elif isOverlapping(s1, e1, s2, e2):
        part2 += 1
      
  print('Part 1: ', part1)
  print('Part 2: ', part2)





  
      

