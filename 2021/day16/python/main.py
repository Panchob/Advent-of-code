
import os
import sys
import pathlib

def hexToBin(data):
  return bin(int(data, 16))[2:].zfill(len(data) * 4)

def decode(data, i):
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
        j, v =  decode(data, i)
        currentL = j - i
        version += v
        packetL -= currentL
        i = j
    else:
      numOfPackets = int(data[i: i + 11], 2)
      i += 11

      while numOfPackets > 0:
        i, v =  decode(data, i)
        version += v
        numOfPackets -= 1
  return (i, version)




if __name__ == '__main__':
  path = pathlib.Path(sys.path[0]).parent
  with open(os.path.join(path, 'input.txt'), "r") as f:
    hexa = f.read()
    
    print(decode(hexToBin('8A004A801A8002F478'), 0))
    print(decode(hexToBin('620080001611562C8802118E34'), 0))
    print(decode(hexToBin('C0015000016115A2E0802F182340'), 0))
    print(decode(hexToBin('A0016C880162017C3686B18A3D4780'), 0))
    print(decode(hexToBin(hexa), 0))

