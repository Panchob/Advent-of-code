import os
import sys
import pathlib

def fileToLines(filename):
  path = pathlib.Path(sys.path[0]).parent
  lines = []
  with open(os.path.join(path, filename), "r") as f:
    for line in f.readlines():
      lines.append(line.strip())
  return lines

def parseData(lines):
  coordinates = {}
  for y in range(len(lines)):
    for x in range(len(lines[y])):
      coordinates[(x, y)] = lines[y][x]
  return coordinates

paths = []

def findAllPathToEnd(coordinates, current, visited, end):
  global paths
  if current in visited or current not in coordinates:
    return
  if current == end:
    paths.append(visited)
    return
  
  visited.append(current)
  findAllPathToEnd(coordinates, (current[0] + 1, current[1]), visited, end)
  findAllPathToEnd(coordinates, (current[0] - 1, current[1]), visited, end)
  findAllPathToEnd(coordinates, (current[0], current[1] + 1), visited, end)
  findAllPathToEnd(coordinates, (current[0], current[1] - 1), visited, end)

if __name__ == '__main__':
  path = pathlib.Path(sys.path[0]).parent
  rawData = fileToLines("test.txt")
  coordinates = parseData(rawData)
  keys = list(coordinates.keys())
  findAllPathToEnd(coordinates, (0, 0), [], keys[-1])
  print(keys[-1])
  print(len(paths))

