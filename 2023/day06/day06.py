import os
import sys

def findRecord(time, distance):
  record = []
  speed = 0
  for i in range(time):
    r = ((time - i) * speed)
    if r > distance:
      record.append(r)
    speed += 1
  return record


def part1(times, distances):
  total = 1
  
  for index, time in enumerate(times):
    total *= len(findRecord(time, distances[index]))
  print('Part 1: ' + str(total))

def part2(times, distances):
  time = int(''.join(times))
  distance = int(''.join(distances))
  record = findRecord(time, distance)


  print('Part 2: ' + str(len(record)))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    filename = sys.argv[1]
  else:
    filename = "input.txt"

  with open(os.path.join(sys.path[0], filename), "r") as f:
    stats = f.read()

    [time, distance] = stats.split("\n")

    time = time.split(": ")[1]
    distance = distance.split(": ")[1]

    time = time.strip()
    distance = distance.strip()

    time = time.split(" ")
    distance = distance.split(" ")

    time = list(map(lambda x: x.strip(), time))
    distance = list(map(lambda x: x.strip(), distance))

    time = list(filter(None, time))
    distance = list(filter(None, distance))

    part2(time, distance)

    time = list(map(int, time))
    distance = list(map(int, distance))

    part1(time, distance)