dial = 50
zeros = 0 #the password is the number of times that the dial points to 0
finish_zero = 0
with open("input1.txt") as file:
    for line in file:
        direction = line[0] # 'L' or 'R'
        num = int(line[1:])
        #for each full rotation the dial passes by zero
        zeros+=abs(num//100)
        rotation = num % 100
        if (rotation != 0): #there's a change in dial's final position
            if direction == 'L':
                if dial - rotation <= 0 and dial != 0: #dial passed through or finished at zero
                    zeros+=1
                dial = (dial - rotation) % 100
            if direction == 'R':
                if dial + rotation >= 100 and dial != 0: #dial passed through or finished at zero
                    zeros+=1
                dial = (dial + rotation) % 100
print("The actual password is:",zeros)

