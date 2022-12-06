import os
import sys

def findFirstMarker(line, length=4):
  for i in range(len(line) - (length - 1)):
    if len(set(line[i:i+length])) == length:
      return i + length
    i += 1


if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    line = f.read()
    print('Part 1: ', findFirstMarker(line))
    print('Part 2: ', findFirstMarker(line, 14))
