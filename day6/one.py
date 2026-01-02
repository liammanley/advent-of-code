# https://adventofcode.com/2025/day/6
#pair programmed with my sister
#refactored to choose reasonable variable names and remove debug prints
day = open("input.txt")
unparsed_data = day.read().splitlines()
day.close()

#construct data array
#the operators in the last row are strings
data = []
for i in range(len(unparsed_data)-1):
  data.append(list(map(int, unparsed_data[i].split())))
data.append(unparsed_data[-1].split())


total = 0
for i in range(len(data[0])):
  current = 0
  if (data[len(data) - 1][i] == "*"):
    current = 1
  for j in range(len(data) - 1):
    if (data[len(data) - 1][i] == "+"):
      current += data[j][i]
    else:
      current *= data[j][i]
  total += current
print(total)