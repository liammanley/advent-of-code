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
###               part 1                        ###
###################################################
for i in range(len(rules)):
  rules[i] = rules[i].split("-")
upper = []
lower = []
for rang in rules:
  lower.append(int(rang[0]))
  upper.append(int(rang[1]))


total = 0
for i in data:
  i = int(i)
  fresh = False
  for j in range(len(lower)):
    if (i <= upper[j] and i >= lower[j]):
      fresh = True
  if fresh:
    total += 1

print(total)
