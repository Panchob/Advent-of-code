import os
import sys
from functools import reduce

grid = []

def checkVisible(x, y, lefts, rights, ups, downs):
  current = grid[x][y]

  if x == 0 or x >= len(grid) -1:
    return 1
  if y == 0 or y >= len(grid[x]) -1:
   return 1

  if all(current > i for i in lefts):
    return 1
  if all(current > i for i in rights):
    return 1
  if all(current > i for i in ups):
    return 1
  if all(current > i for i in downs):
    return 1
  return 0

def viewingDistance(x, y, lefts, rights, ups, downs):
  current = grid[x][y]
  distances = {
    "left": 0,
    "right": 0,
    "up": 0,
    "down": 0,
  }

  distances['left'] = viewingInDirection(lefts, current)
  distances['right'] = viewingInDirection(rights, current)
  distances['up'] = viewingInDirection(ups, current)
  distances['down'] = viewingInDirection(downs, current)

  values = list(filter(lambda x: x > 0, distances.values()))
  print(current, reduce(lambda x, y: x * y, values))
  return reduce(lambda x, y: x * y, values)



def viewingInDirection(direction, current):
  distance = 0

  if len(direction) == 0:
    return 0
  for i in range(len(direction)):
    distance += 1
    if direction[i] >= current:
      break
      
  
  return distance

if __name__ == '__main__':
  visible = 0
  viewingScore = []
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f.readlines():
      row = []
      for char in line.strip():
        row.append(int(char))
      grid.append(row)

    for x in range(len(grid)):
      for y in range(len(grid[x])):
        lefts = grid[x][:y]
        lefts.reverse()
        rights = grid[x][y + 1:]
        ups = [row[y] for row in grid[:x]]
        ups.reverse()
        downs = [row[y] for row in grid[x + 1:len(grid)]]
        visible += checkVisible(x, y, lefts, rights, ups, downs)
        viewingScore.append(viewingDistance(x, y, lefts, rights, ups, downs))
    print(visible)
    print(max(viewingScore))
    
      
      


