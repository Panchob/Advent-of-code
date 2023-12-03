import os
import sys

if __name__ == '__main__':
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    cycle = 1
    X = 1
    cycleToCheck = 20
    total = 0
    rows = [[] for i in range(7)]
    currentRow = 0
    print(rows)

    for line in lines:
      position = (cycle - 1) % 40
      if (position) == X -1 or (position) == X + 1 or (position) == X:
        rows[currentRow].append('#')
      else:
        rows[currentRow].append(' ')
      currentRow += 1 if cycle % 40 == 0 else 0
      if line.strip() == 'noop':
        cycle += 1
      else:
        cycle += 1
        position = (cycle - 1) % 40
        if (position) == X -1 or (position) == X + 1 or (position) == X:
          rows[currentRow].append('#')
        else:
          rows[currentRow].append(' ')
        
        currentRow += 1 if cycle % 40 == 0 else 0

        if cycle == cycleToCheck:
          total += X * cycleToCheck
          cycleToCheck += 40

        X += int(line.split(' ')[1])
        cycle += 1


      if cycle == cycleToCheck:
        total += X * cycleToCheck
        cycleToCheck += 40
      
    
    print(total)
    for row in rows:
      print(' '.join(row))
      
          


    


    
      
      


