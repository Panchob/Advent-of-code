import sys
import os

def parse(line):
  content = line.strip().split(" ")
  content = list(map(lambda x: x.strip(), content))
  return list(map(int, content))


def part1(almanac):
  instructions = almanac.split("\n\n")
  seeds = parse(instructions[0].split(': ')[1])
  nextStep = seeds.copy()

  for instruction in instructions[1:]:
    [_, content] = instruction.split(":\n")
    lines = content.split("\n")
    for line in lines:
      [des,sou,ran] = parse(line)
      for index, seed in enumerate(seeds):
        if seed >= sou and seed <= sou + ran:
          nextStep[index] = des + (seed - sou)
      
    seeds = nextStep.copy()
  print('Part 1: ' + str(min(seeds)))

def part2(almanac):
  instructions = almanac.split("\n\n")
  parsed = parse(instructions[0].split(': ')[1])
  seeds = []

  i = 0
  while i < len(parsed):
    seeds.append({
      'start': parsed[i],
      'end': parsed[i] + parsed[i + 1]
    })
    i += 2

  for instruction in instructions[1:]:
    [_, content] = instruction.split(":\n")
    lines = content.split("\n")
    i = 0
    while i < len(seeds):
      start, end = seeds[i]["start"], seeds[i]["end"]
      block = False
      for line in lines:
        [des,sou,ran] = parse(line)

        if start >= sou and start < (sou + ran) and not block:
          block = True
          seeds[i]["start"] = des + (start - sou)

          if end < (sou + ran):
            seeds[i]['end'] = des + (end - sou)
          else:
            seeds[i]['end'] = des + ran - 1
            seeds.append({
              'start': sou + ran,
              'end': end
            })
        elif end >= sou and end < (sou + ran) and not block:
          block = True
          seeds[i]['end'] = des + (end - sou)

          if start > sou:
            seeds[i]["start"] = des + (start - sou)
          else:
            seeds[i]["start"] = des
            seeds.append({
              'start': start,
              'end': sou - 1
            })
      i += 1
  
  starts = list(map(lambda x: x["start"], seeds))
  print('Part 2: ' + str(min(starts)))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"

  with open(os.path.join(sys.path[0], filename), "r") as f:
    almanac = f.read()
    part1(almanac)
    part2(almanac)