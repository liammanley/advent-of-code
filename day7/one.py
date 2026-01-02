day = open("input.txt")
data = day.read()
day.close()
data = data.splitlines()

grid = []
for line in data:
  grid.append(list(line))

#change S to |
for i in range(len(grid[0])):
  if grid[0][i] == 'S':
    grid[0][i] = '|'

for i in range(1, len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '.' and grid[i - 1][j] == '|':
      grid[i][j] = '|'
    if grid[i][j] == '^' and grid[i - 1][j] == '|':
      grid[i][j - 1] = '|'
      grid[i][j + 1] = '|'

total = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '^' and grid[i - 1][j] == '|':
      total += 1
print(total)