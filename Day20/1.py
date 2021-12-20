import os, sys, time
def printGrid(grid):
  for row in grid:
    string = ""
    for cell in row:
      string += "#" if cell else "."
    print(string)

def getIndex(grid, i, j, default):
  numbers = [-1 for i in range(9)]
  if i == 0:
    numbers[0]=default*256
    numbers[1]=default*128
    numbers[2]=default*64
  elif i +1 == len(grid):
    numbers[6] = default*4
    numbers[7] = default*2
    numbers[8] = default
  if j == 0:
    numbers[0] = default*256
    numbers[3] = default*32
    numbers[6] = default*4
  elif j +1 == len(grid[i]):
    numbers[2] = default*64
    numbers[5] = default*8
    numbers[8] = default
  counter = 0
  for x in range(-1,2):
    for y in range(-1,2):
      if numbers[counter] == -1:
        numbers[counter] = grid[i+x][j+y]*pow(2,8-counter) 
      counter += 1
  return sum(numbers)

def doStep(grid, imageAlg, default):
  newGrid = [row[:] for row in grid]
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      index = getIndex(grid, i, j, default)
      newGrid[i][j] = imageAlg[index]
  return newGrid

def extendGrid(grid, number, default):
  oldLength = len(grid[0])
  for row in grid:
    for i in range(number):
      row.insert(0, default)
      row.append(default)
  grid.insert(0, [default for i in range(oldLength+number*2)])
  grid.append([default for i in range(oldLength + number*2)])

def traverseImage(grid, imageAlg):
  newGrid = doStep(grid, imageAlg, grid[0][0])
  extendGrid(newGrid, 1, newGrid[0][0])
  return newGrid

def main():
  inputText = open(os.path.join(sys.path[0], 'input'), 'r')
  lines = inputText.readlines()

  imageAlg = [char == "#" for char in lines[0].strip()]

  grid = []
  for line in lines[2:]:
    row = [char == "#" for char in line.strip()]
    grid.append(row)
  extendGrid(grid, 1, False)
  # printGrid(grid)
  for i in range(50):
    grid = traverseImage(grid, imageAlg)
    # printGrid(grid)
  counter = 0
  for row in grid:
    for cell in row:
      if cell:
        counter += 1
  print(counter)

if __name__ == "__main__":
  t = time.time()
  main()
  print (time.time() - t)