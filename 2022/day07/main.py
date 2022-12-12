import os
import sys

filesystem = {'ROOT':{'files':[], 'parent': None, 'dirs':[]}}

def totalDirSize(current):
  if 'size' in filesystem[current].keys():
    return filesystem[current]['size']

  size = sum([file['size'] for file in filesystem[current]['files']])
  if len(filesystem[current]['dirs']) == 0:
    filesystem[current]['size'] = size
    return size
  for dir in filesystem[current]['dirs']:
    size += totalDirSize(dir)
  filesystem[current]['size'] = size
  return size

def sizeUnder(size):
  total = 0
  for dir in filesystem:
    if filesystem[dir]['size'] <= size:
      total += filesystem[dir]['size']
  return total

def smallestToDeleteUnder():
  dirs = []
  currentUnused = 70000000 - filesystem['ROOT']['size']
  for dir in filesystem:
    if currentUnused + filesystem[dir]['size'] >= 30000000:
      dirs.append((filesystem[dir]['size']))
  print(dirs)
  return min(dirs)


if __name__ == '__main__':
  current = 'ROOT'
  with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f.readlines()[2::]:
      line = line.strip()
      if 'dir' in line:
        newDir = current + '/' + line.split(' ')[1]
        filesystem[current]['dirs'].append(newDir)
        filesystem[newDir] = {'files':[], 'parent': current, 'dirs':[]}
      elif line[0] == '$':
        if line.split(' ')[1] == 'cd':
          if line.split(' ')[2] == '..':
            current = filesystem[current]['parent']
          else:
            current = current + '/' + line.split(' ')[2]
      else:
        size, name = line.split(' ')
        filesystem[current]['files'].append({'name':name, 'size': int(size)})
  
  for dir in filesystem.keys():
    totalDirSize(dir)
      
  part1 = sizeUnder(100000)

  print('Part 1:', part1)

  part2 = smallestToDeleteUnder()

  print('Part 2:', part2)
    
      
      


