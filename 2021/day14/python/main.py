import os
import sys
import pathlib

def fileToLines(filename):
  path = pathlib.Path(sys.path[0]).parent
  lines = []
  with open(os.path.join(path, filename), "r") as f:
    for line in f.readlines():
      lines.append(line.strip())
  return lines

def parseData(lines):
  parsedData = {
    'template': '',
    'formulas': {},
  }
  parsedData['template'] = lines[0]
  for line in lines[2:]:
    parsedData['formulas'][line.split(' -> ')[0]] = line.split(' -> ')[1]
  return parsedData
  
def splitTemplateInPairs(template):
  pairs = {}
  for i in range(0, len(template)):
    pair = template[i:i+2]
    if len(pair) < 2:
      break
    if pair in pairs:
      pairs[pair] += 1
    else:
      pairs[pair] = 1
  return pairs

def splitTemplateInLetters(template):
  letters = {}
  for letter in template:
    if letter in letters:
      letters[letter] += 1
    else:
      letters[letter] = 1
  return letters

def generatePolymer(pairs, formulas, letters, cycleCount):
  for i in range(cycleCount):
    pairsSnapshot = pairs.copy()
    for pair in pairsSnapshot:
      if pairsSnapshot[pair] > 0:
        newLetter = formulas[pair]
        if newLetter in letters:
          letters[newLetter] += pairsSnapshot[pair]
        else:
          letters[newLetter] = pairsSnapshot[pair]
        newPairs = [pair[0] + newLetter, newLetter + pair[1]]
        for newPair in newPairs:
          if newPair in pairs:
            pairs[newPair] += pairsSnapshot[pair]
          else:
            pairs[newPair] = pairsSnapshot[pair]
        pairs[pair] -= pairsSnapshot[pair]
  return [pairs, letters]

if __name__ == '__main__':
  path = pathlib.Path(sys.path[0]).parent
  rawData = fileToLines("input.txt")
  parsedData = parseData(rawData)
  pairs = splitTemplateInPairs(parsedData['template'])
  letters = splitTemplateInLetters(parsedData['template'])
  [pairs, letters] = generatePolymer(pairs, parsedData['formulas'], letters,  40)
  print(max(letters.values()) - min(letters.values()))

