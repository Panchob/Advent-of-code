import os
import sys
from functools import reduce

if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"


  def part1(lines):
    MAX_COLORS ={
      "red": 12,
      "green": 13,
      "blue": 14,
    }

    total = 0
    index = 1
    addIt = True

    for line in lines:
      [_, games] = line.split(":")
      addIt = True

      for game in games.strip().split(";"):
        for instance in game.split(","):
          [value, color] = instance.strip().split(" ")
          if int(value) > MAX_COLORS[color]:
            addIt = False
            break
      if addIt:
        total += index
      index += 1

    print('Part 1:', total)

  def part2(lines):
    total = 0

    for line in lines:
      [_, games] = line.split(":")
      minColors = {
        "red": 1,
        "green": 1,
        "blue": 1,
      }

      for game in games.strip().split(";"):
        for instance in game.split(","):
          [value, color] = instance.strip().split(" ")
          if int(value) > minColors[color]:
            minColors[color] = int(value)

      total += reduce((lambda x, y: x * y), minColors.values())

    print('Part 2:', total)


  with open(os.path.join(sys.path[0], filename), "r") as f:
    lines = f.read().split("\n")
    part1(lines)
    part2(lines)