import os
import sys
from copy import deepcopy

OPERATORS = {
  "*": lambda x, y: x * y,
  "+": lambda x, y: x + y,
}

def parseOperation(operation, old):
  first, operator, second = operation.split(" ")
  first = old if first == "old" else int(first)
  second = old if second == "old" else int(second)
  return OPERATORS[operator](first, second)

def smallestCommon(monkeys):
  res = 1
  for monkey in monkeys:
    res *= monkey["test"]
  return res

def part1(monkeys):
  for _ in range(20):
    for monkey in monkeys:
      for item in monkey["items"]:
        worry = parseOperation(monkey["operation"], item)
        worry = worry // 3
        if worry % monkey["test"] == 0:
          monkeys[monkey["true"]]["items"].append(worry)
        else:
          monkeys[monkey["false"]]["items"].append(worry)
      monkey['inspected'] += len(monkey['items'])
      monkey['items'] = []
    
  
  for i in range(len(monkeys)):
    print(f'Monkey {i}: {monkeys[i]["inspected"]}')

def part2(monkeys, modulo):
  for _ in range(10000):
    for monkey in monkeys:
      for item in monkey["items"]:
        worry = parseOperation(monkey["operation"], item)
        worry = worry % modulo
        if worry % monkey["test"] == 0:
          monkeys[monkey["true"]]["items"].append(worry)
        else:
          monkeys[monkey["false"]]["items"].append(worry)
      monkey['inspected'] += len(monkey['items'])
      monkey['items'] = []
    
  
  for i in range(len(monkeys)):
    print(f'Monkey {i}: {monkeys[i]["inspected"]}')




if __name__ == '__main__':
  current = 1
  MONKEYS = []
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()
    while current < len(lines):
      currentMonkey = {}
      items = lines[current].split(": ")[1].split(", ")
      currentMonkey["items"] = list(map(int, items))
      current += 1
      currentMonkey["operation"] = lines[current].split(" = ")[1]
      current += 1
      currentMonkey["test"] = int(lines[current].split(" ")[-1])
      current += 1
      currentMonkey["true"] = int(lines[current].split(" ")[-1])
      current += 1
      currentMonkey["false"] = int(lines[current].split(" ")[-1])
      current += 3
      currentMonkey["inspected"] = 0
      MONKEYS.append(currentMonkey)

  p = deepcopy(MONKEYS)
  part1(p)
  modulo = smallestCommon(MONKEYS)
  print(modulo)
  part2(MONKEYS, modulo)



      
          


    


    
      
      


