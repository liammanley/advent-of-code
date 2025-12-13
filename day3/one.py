#problem: https://adventofcode.com/2025/day/3

def highest_joltage(bank):
    #find the tens digit: the biggest value in the bank that's not the last entry
    big = bank[0]
    big_index = 0
    for i in range(len(bank)-1):
        if bank[i] > big:
            big = bank[i]
            big_index = i
    #find the ones digit: the biggest value in the bank that's after big
    ones_digit = bank[big_index+1]
    for i in range(big_index+1, len(bank)):
        if bank[i]>ones_digit:
            ones_digit = bank[i]
    return 10 * big + ones_digit

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        total = 0
        for line in file:
            #I want bank to be immutable, so I'm using a tuple instead of a list
            bank = tuple(int(c) for c in line.strip())
            total+=highest_joltage(bank)
    print(total)
