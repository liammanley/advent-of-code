# https://adventofcode.com/2025/day/4
# pair programmed with my sister, Audrey Manley

day4 = open("input.txt")
day4data = day4.read()
day4.close()
data = day4data.split()

for i in range(len(data)):
  data[i] = list(data[i])
# loop through rows
# row i index j
# for each position, check if there is a roll
# if there is a roll:
# check l, r, u, d, etc
# if < 4 add one to counter
# sides:
# if i = 0 (top row): dont check u, ul, ur
# if i = len(data) - 1: dont check d, dl, dr
# if j = 0 (left): dont check l, ul, dl
# if j = len(row) - 1 (right): dont check r, ur, dr

total = 3000
realtotal = 0
while total != 0:
  total = 0
  for i in range(len(data)):
    row = data[i]
    for j in range(len(row)):
      howmany = 0
      # ul
      if (i != 0 and j != 0 and data[i - 1][j - 1] == "@"):
        howmany += 1
      # u
      if (i != 0 and data[i - 1][j] == "@"):
        howmany += 1
      # ur
      if (i != 0 and j != len(row) - 1 and data[i - 1][j + 1] == "@"):
        howmany += 1
      # l
      if (j != 0 and data[i][j - 1] == "@"):
        howmany += 1
      # r
      if (j != len(row) - 1 and data[i][j + 1] == "@"):
        howmany += 1
      # dl
      if (i != len(data) - 1 and j != 0 and data[i + 1][j - 1] == "@"):
        howmany += 1
      # d
      if (i != len(data) - 1 and data[i + 1][j] == "@"):
        howmany += 1
      # dr
      if (i != len(data) - 1 and j != len(row) - 1
          and data[i + 1][j + 1] == "@"):
        howmany += 1
      if (howmany < 4 and data[i][j] == "@"):
        total += 1 * 10**0
        data[i][j] = "X"
  realtotal += total
print(realtotal)
