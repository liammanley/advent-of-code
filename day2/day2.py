# https://adventofcode.com/2025/day/2
def is_repeated_n_times(s,n):
    sz = len(s)//n
    sub = s[0:sz]
    for i in range(n):
        #print(s[i*n:i*n+sz])
        if s[i*sz:i*sz+sz]!=sub:
            return False
    return True
    
x=is_repeated_n_times("123412345",2)
print(x)

def is_valid_id(id):
    s = str(id)
    for i in range(2,len(s)//2+1):
        if len(s)%i:
            continue
        if is_repeated_n_times(s,i):
            print(s,i)
            return True
    #case: all values in s are the same
    for c in s:
        if s[0]!=c:
            return False
    return True if len(s)!=1 else False

if __name__=="__main__":
    with open("input.txt") as file:
        bigTotal = 0
        for line in file:
            intervals = line.split(",")
            for interval in intervals:
                low, high = map(int, interval.split("-"))
                for id in range(low, high+1):
                    if is_valid_id(id):
                        #print(id)
                        bigTotal+=id
    print(bigTotal)
