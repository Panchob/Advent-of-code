import numpy as np
import math
import os
import sys
from collections import defaultdict


def asteroidCount(arr, curr):
   angles = defaultdict(list)

   for y in range(len(arr)):
      for x in range(len(arr[0])):
         if arr[y][x] == '#' and (x, y) != curr:
            deg = math.degrees(math.atan2((len(arr) - y) - (len(arr) - curr[1]), x - curr[0]))
            angles[deg].append((x, y))

   return(angles)


def sortAnglesAsCircle(angles):
   quadrants = defaultdict(list)

   for angle in angles:
      if(angle <= 90 and angle > 0):
         quadrants[0].append(angle)
      elif(angle <= 0 and angle > -90):
         quadrants[1].append(angle)
      elif(angle <= -90 ):
         quadrants[2].append(angle)
      else:
         quadrants[3].append(angle)

   circle = []
   # Start and finishes at 90, decreasing
   for i in range(4):
      quadrants[i].sort(reverse=True)
      circle += quadrants[i]

   return circle


def getClosestAsteroid(asteroids, station):
      closestDistance = 0
      closestAsteroid = asteroids[0]
      for x, y in asteroids:
         d = abs(x - station[0]) + abs( y - station[1])

         if closestDistance == 0 or d < closestDistance:
            closestDistance = d
            closestAsteroid = (x, y)

      return closestAsteroid


if __name__ == "__main__":
   with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
      matrix = []
      for line in f:
         for c in line.splitlines():
            matrix.append(c)
      arr = np.array(matrix)

   station = (0,0)
   angles = []
   maxCount = 0
   for y in range(len(arr)):
      total = []
      for x in range(len(arr[0])):
         if arr[y][x] == '#':
            total = asteroidCount(arr, (x, y))
            if len(total) > maxCount:
               maxCount = len(total)
               angles = total
               station = (x, y)


   circle = sortAnglesAsCircle(angles)
   ans = circle[199]
   asteroids = angles[ans]
   (x, y) = getClosestAsteroid(asteroids, station)

   print("Part 1:", len(angles))
   print("Part 2:", (x * 100) + y)


