
import os
import sys
import pathlib
import math

operations = [
  lambda a: sum(a),
  lambda a: math.prod(a),
  lambda a: min(a),
  lambda a: max(a),
  '',
  lambda a: int(a[0] > a[1]),
  lambda a: int(a[0] < a[1]),
  lambda a: int(a[0] == a[1]),
]

def hexToBin(data):
  return bin(int(data, 16))[2:].zfill(len(data) * 4)

def decodeVersion(data, i):
  version = 0
  version += int(data[i: i + 3], 2)
  i += 3
  type = int(data[i: i + 3], 2)
  i += 3

  if type == 4:
    literal = ''
    while True:
      literal += data[i+1:i+5]
      if data[i] == '0':
        break
      i += 5
    i += 5
  else:
    lengthType = data[i]
    i += 1

    if lengthType == '0':
      packetL = int(data[i: i + 15], 2)
      i += 15

      while packetL > 0:
        j, v =  decodeVersion(data, i)
        currentL = j - i
        version += v
        packetL -= currentL
        i = j
    else:
      numOfPackets = int(data[i: i + 11], 2)
      i += 11

      while numOfPackets > 0:
        i, v =  decodeVersion(data, i)
        version += v
        numOfPackets -= 1
  return (i, version)

def decode(data, i):
  i += 3
  type = int(data[i: i + 3], 2)
  i += 3
  literal = ''

  if type == 4:
    while True:
      literal += data[i+1:i+5]
      if data[i] == '0':
        break
      i += 5
    i += 5
    literal = int(literal, 2)
  else:
    lengthType = data[i]
    i += 1
    literals = []

    if lengthType == '0':
      packetL = int(data[i: i + 15], 2)
      i += 15

      while packetL > 0:
        j, l =  decode(data, i)
        literals.append(l)
        currentL = j - i
        packetL -= currentL
        i = j
    else:
      numOfPackets = int(data[i: i + 11], 2)
      i += 11

      while numOfPackets > 0:
        i, l =  decode(data, i)
        literals.append(l)
        numOfPackets -= 1
    literal = operations[type](literals)
  return (i, literal)




if __name__ == '__main__':
  path = pathlib.Path(sys.path[0]).parent
  with open(os.path.join(path, 'input.txt'), "r") as f:
    hexa = f.read()
    print('Part 1:', decodeVersion(hexToBin(hexa), 0)[1])
    print('Part 2', decode(hexToBin(hexa), 0)[1])

