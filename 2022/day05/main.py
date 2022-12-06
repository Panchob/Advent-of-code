import os
import sys

def createStacks(firstPart):
  stacks = {}
  for line in firstPart.split('\n')[:-1]:
    pos = 1
    col = 1
    while pos < len(line):
      if line[pos].isalpha():
        if col not in stacks:
          stacks[col] = []
        stacks[col].insert(0, line[pos])
      col += 1
      pos += 4
  return stacks

def part1(stacks, instructions):
    for line in instructions.split('\n'):
      instruction, positions = line.split(' from ')
      numOfCrates = int(instruction.split(' ')[1])
      start, end = map(int, positions.split(' to '))
      for i in range(numOfCrates):
        stacks[end].append(stacks[start].pop())
    
    ans = ''
    for i in range(1, len(stacks)+1):
      ans += stacks[i].pop()
    return ans

def part2(stacks, instructions):
    for line in instructions.split('\n'):
      instruction, positions = line.split(' from ')
      numOfCrates = int(instruction.split(' ')[1])
      start, end = map(int, positions.split(' to '))
      stacks[end] += stacks[start][-numOfCrates:]
      del stacks[start][-numOfCrates:]
    
    ans = ''
    for i in range(1, len(stacks)+1):
      ans += stacks[i].pop()
    return ans

if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    firstPart, secondPart = f.read().split('\n\n')
    print(part1(createStacks(firstPart), secondPart))
    print(part2(createStacks(firstPart), secondPart))
