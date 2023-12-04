import os
import sys

def checkAdjacentLines(scheme, position):
  [x, y] = position
  lines = [y-1, y, y+1]
  total = 0
  maxX = len(scheme[0])


  for line in lines:
    currentNum = 0
    isAdjacent = False
    charX = 0
    if line < 0 or line >= len(scheme):
      continue
    for char in scheme[line]:
      if char.isdigit():
        currentNum *= 10
        currentNum += int(char)
        if charX in [x-1, x, x+1]:
          isAdjacent = True
      elif currentNum > 0:
        if isAdjacent:
          total += currentNum
          numLen = len(str(currentNum))
          replacement = "." * numLen
          scheme[line] = scheme[line][:charX-numLen] + replacement + scheme[line][charX:]
          isAdjacent = False
        currentNum = 0
      # end of line
      if charX == maxX - 1 and currentNum > 0 and isAdjacent:
        total += currentNum
        numLen = len(str(currentNum))
        scheme[line] = scheme[line].replace(str(currentNum), ".")
        replacement = "." * numLen
        scheme[line] = scheme[line][:charX-numLen] + replacement + scheme[line][charX:]
        isAdjacent = False
      charX += 1
  return total

def checkAdjacentLines2(scheme, position):
  [x, y] = position
  lines = [y-1, y, y+1]
  total = 0
  maxX = len(scheme[0])
  adjacents = []


  for line in lines:
    currentNum = 0
    isAdjacent = False
    charX = 0

    if line < 0 or line >= len(scheme):
      continue
    for char in scheme[line]:
      if char.isdigit():
        currentNum *= 10
        currentNum += int(char)
        if charX in [x-1, x, x+1]:
          isAdjacent = True
      elif currentNum > 0:
        if isAdjacent:
          adjacents.append({
            "num": currentNum,
            "x": charX,
            "y": line
          })
          isAdjacent = False
        currentNum = 0
      # end of line
      if charX == maxX - 1 and currentNum > 0 and isAdjacent:
        adjacents.append({
          "num": currentNum,
          "x": charX,
          "y": line
        })
        isAdjacent = False
      charX += 1

  if len(adjacents) == 2:
    total += adjacents[0]["num"] * adjacents[1]["num"]
    for adjacent in adjacents:
      numLen = len(str(adjacent["num"]))
      replacement = "." * numLen
      scheme[adjacent["y"]] = scheme[adjacent["y"]][:adjacent["x"]-numLen] + replacement + scheme[adjacent["y"]][adjacent["x"]:]
  return total


def part1(scheme):
  lines = scheme.split("\n")
  total = 0
  y = 0
  x = 0
  for line in lines:
    for char in line:
      # Find a symbol
      if not (char.isalpha() or char.isdigit()) and char != ".":
        position = [x, y]
        total += checkAdjacentLines(lines, position)
      x += 1
    y += 1
    x = 0
  print('Part 1:', total)

def part2(scheme):
  lines = scheme.split("\n")
  total = 0
  y = 0
  x = 0
  for line in lines:
    for char in line:
      # Find a symbol
      if not (char.isalpha() or char.isdigit()) and char != ".":
        position = [x, y]
        total += checkAdjacentLines2(lines, position)
      x += 1
    y += 1
    x = 0
  print('Part 2:', total)



if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"

  with open(os.path.join(sys.path[0], filename), "r") as f:
    scheme = f.read()
    part1(scheme)
    part2(scheme)