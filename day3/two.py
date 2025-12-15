#problem: https://adventofcode.com/2025/day/3

#returns largest element and index of largest element in arr[start:end]
#remember that end is not included
def max_and_index_sub_arr(arr, start, end):
    big = arr[start]
    big_index = start
    for i in range(start, end):
        num=arr[i]
        if num > big:
            big = num
            big_index = i
    return (big, big_index)

#each call to highest_joltage finds the highest (digits_remaining) digit joltage starting at first_index
def highest_joltage(bank, digits_remaining, first_index):
    #base case: digits remaining==0, we're done
    if digits_remaining==0:
        return 0
    #find the largest digit that we are allowed to pick
    #the digit at len(bank)-digits_remaining+1 is not allowed
    #because then there would be no values to the right of it to turn on
    big, big_index = max_and_index_sub_arr(bank, first_index, len(bank)-digits_remaining+1)
    #highest_joltage gives the joltage from the numbers to the right.
    #big * (10**(digits_remaining-1)) adds the digit we picked in the right decimal place
    return big * (10**(digits_remaining-1)) + highest_joltage(bank, digits_remaining-1, big_index+1)

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        total = 0
        for line in file:
            #I want bank to be immutable, so I'm using a tuple instead of a list
            bank = tuple(int(c) for c in line.strip())
            total+=highest_joltage(bank=bank, digits_remaining=12, first_index=0)
    print(total)
