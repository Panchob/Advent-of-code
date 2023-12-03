import os
import sys

LETTERED_NUMBER = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def getLetteredNum(string):
  if len(string) >= 3 and string[0:3] in LETTERED_NUMBER:
    return LETTERED_NUMBER[string[0:3]]
  elif len(string) >= 4 and string[0:4] in LETTERED_NUMBER:
    return LETTERED_NUMBER[string[0:4]]
  elif len(string) >= 5 and string[0:5] in LETTERED_NUMBER:
    return LETTERED_NUMBER[string[0:5]]
  return ''


def getFirstDigit(string):
  for char in string:
    if char.isdigit():
      return char

def getLastDigit(string):
  for char in reversed(string):
    if char.isdigit():
      return char

def part1(lines):
  total = 0
  for line in lines:
    value = getFirstDigit(line) + getLastDigit(line)
    total += int(value)
  print('Part 1:', total)

def getFirst(string):
  index = 0
  for char in string:
    current = ''
    if char.isalpha():
      current = getLetteredNum(string[index:])
    else:
      current = char
    if current != '':
      return current
    index += 1
  
def getLast(string):
  index = 0
  reversedLine = string[::-1]
  for char in reversedLine:
    current = ''
    if char.isalpha():
      current = getLetteredNum(string[len(string) - index - 1:])
    else:
      current = char
    if current != '':
      return current
    index += 1
    

def part2(lines):
  total = 0
  for line in lines:
    first = getFirst(line)
    last = getLast(line)
    total += int(first + last)
  print('Part 2:', total)

if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().split("\n")
    part1(lines)
    part2(lines)

