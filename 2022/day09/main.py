import os
import sys

moveInDirections = {
  "U": lambda x, y: (x, y + 1),
  "D": lambda x, y: (x, y - 1),
  "L": lambda x, y, : (x - 1, y),
  "R": lambda x, y: (x + 1, y)
}

def areTouching(t, h):
  if t == h:
    return True
  if t[0] == h[0] and abs(t[1] - h[1]) == 1:
    return True
  if t[1] == h[1] and abs(t[0] - h[0]) == 1:
    return True
  if abs(t[0] - h[0]) == 1 and abs(t[1] - h[1]) == 1:
    return True
  return False

  


def moveCloser(t, h):
  deltaX = 0
  deltaY = 0

  if t[0] < h[0]:
    deltaX = 1
  elif t[0] > h[0]:
    deltaX = -1

  if t[1] < h[1]:
    deltaY = 1
  elif t[1] > h[1]:
    deltaY = -1

  return (t[0] + deltaX, t[1] + deltaY)

if __name__ == '__main__':
  h = (0, 0)
  t = (0, 0)  
  s = (0, 0)
  visited = set((0,0))

  with open(os.path.join(sys.path[0], "test.txt"), "r") as f:
    lines = f.readlines()
    for line in lines:
      direction, step = line[0], int(line[1:])
      for i in range(step):
        h = moveInDirections[direction](*h)
        if not areTouching(t, h):
          t = moveCloser(t, h)
          visited.add(t)
      
    print('part 1:', len(visited))

    visited = set((0,0))
    h = (0, 0)
    tails = [(0, 0)] * 9

    for line in lines:
      direction, step = line[0], int(line[1:])
      for i in range(step):
        h = moveInDirections[direction](*h)
        current = h
        for i in range(len(tails)):
          if areTouching(tails[i], current):
            break
          else:
            tails[i] = moveCloser(tails[i], current)
            current = tails[i]
            if i == 8:
              visited.add(tails[i])
    print('part 2 :', len(visited))


    


    
      
      


