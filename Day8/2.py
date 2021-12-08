import os, sys, re
from typing import DefaultDict
inputText = open(os.path.join(sys.path[0], 'input'), 'r')
lines = inputText.readlines()

def getRemovedSegments(segments: "str", decoded: "str"):
  testSegments = list(segments)
  for segment in decoded:
    if segment in testSegments: testSegments.remove(segment)
  return len(testSegments)


uniqueValues = [2, 4, 3, 7]
unique = { 2: 1, 4: 4, 3: 7, 7: 8}
sum = 0

for line in lines:
  decoded = {}
  parts = line.strip().split(' | ')
  part1Numbers = parts[0].split(' ')
  part2Numbers = parts[1].split(' ')

# for each number in segments
  for part in part1Numbers:
    if len(part) in uniqueValues:
      decoded[unique[len(part)]] = part
  for part in part1Numbers:
    if len(part) not in uniqueValues:
      if getRemovedSegments(part, decoded[1]) == 3:
        decoded[3] = part
      elif getRemovedSegments(part, decoded[7]) == 4:
        decoded[6] = part
      elif len(part) == 6:
        if getRemovedSegments(part, decoded[4]) == 3:
          decoded[0] = part
        else:
          decoded[9] = part
      else:
        if getRemovedSegments(part, decoded[4]) == 3:
          decoded[2] = part
        else:
          decoded[5] = part
         
  totalNumber = 0
  power = 3
  for part2 in part2Numbers:
    foundValue = -1
    # for all decoded Values
    for decodedKey in decoded:
      # if length fits
      if "".join(sorted(decoded[decodedKey])) == "".join(sorted(part2)): 
        foundValue = decodedKey
        break
    totalNumber += foundValue * pow(10, power)
    power -= 1
  print(totalNumber)
  sum += totalNumber
print(sum)

