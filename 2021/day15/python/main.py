
import os
import sys
import pathlib
from numpy import Inf
import heapq

def expandChart(chart):
  l = len(chart)
  extendedChart = [[0 for _ in range(l * 5)] for _ in range(l * 5)] 

  for i, y in enumerate(extendedChart):
    for j in range(0, len(y)):
      baseWeight = chart[i % l][j % l]
      iteratedWeight = baseWeight + ((i // l) + (j // l) - 1) 
      extendedChart[i][j] = iteratedWeight % 9 + 1
  
  return extendedChart


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def getNeighbours(node, maxLength):

    x = node[0]
    y = node[1]
    neighbours = []

    newPositions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    for i in newPositions:
        if (0 <= i[0] <= maxLength - 1) and (0 <= i[1] <= maxLength - 1):
            neighbours.append(i)
    return neighbours

def astar(chart, maxLength):
    start = (0, 0)
    end = (maxLength - 1, maxLength - 1)
    opened = []
    closed = set()
    parents = {}
    weights = {}
    
    for y in range(len(chart)):
        for x in range(len(chart)):
            weights[(y, x)] = Inf
    
    weights[start] = 0
    heapq.heappush(opened, (distance(start, end), start))

    while opened:

      _, current = heapq.heappop(opened)

      if current == end:
        total = 0

        while current in parents:
          total += chart[current[0]][current[1]]
          current = parents[current]
        return total
      
      if current in closed:
        continue

      neighbours = getNeighbours(current, maxLength)

      for neighbour in neighbours:
        if neighbour in closed:
          continue

        totalWeight = weights[current] + chart[neighbour[0]][neighbour[1]]

        if totalWeight <= weights[neighbour]:
          weights[neighbour] = totalWeight
          parents[neighbour] = current
          heapq.heappush(opened, (distance(neighbour, end) + totalWeight , neighbour))
      
      closed.add(current)




if __name__ == '__main__':
    path = pathlib.Path(sys.path[0]).parent
    with open(os.path.join(path, 'input.txt'), "r") as f:
        chart = [[int(i) for i in j] for j in f.read().splitlines()]

    maxLength = len(chart[0])

    part1 = astar(chart, maxLength)
    print('Part 1 :', part1)
    part2 = astar(expandChart(chart), maxLength * 5)
    print('Part 2 :', part2)

