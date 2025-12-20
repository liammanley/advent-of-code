# https://adventofcode.com/2025/day/5
# Pair programmed with my sister, Audrey Manley
# Note: split given input into two files: ranges.txt and values.txt

day5 = open("values.txt")
day5data = day5.read()
day5.close()
data = day5data.split()
for i in range(len(data)):
  data[i] = int((data[i]))

day51 = open("ranges.txt")
day51data = day51.read()
day51.close()
rules = day51data.split()

###################################################
###           part 2                    ###
###################################################

for i in range(len(rules)):
  rang = rules[i]
  rules[i] = rang.split("-")
  for j in range(len(rules[i])):
    rules[i][j] = int(rules[i][j])
  rules[i] = tuple(rules[i])

rules.sort()

# add tuple 0 to reallist realest
realest = [list(rules[0])]
for i in range(1, len(rules)):
  # rules[i] is a tuple ! !
  if (rules[i][0] <= realest[len(realest) - 1][1]):
    if rules[i][1] > realest[len(realest) - 1][1]:
      realest[len(realest) - 1][1] = rules[i][1]
  else:
    realest.append(list(rules[i]))

total = 0
for rang in realest:
  total += rang[1] - rang[0] + 1
print(total)
