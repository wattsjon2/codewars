#Each action takes a set amount of time:

#remove one screw : 1 second
#move to the next screw: 1 second
#switch screwdrivers: 5 seconds

def sc(s):
    time = 0
    previous = s[0]
    for i in range(len(s)):
        if previous != s[i]:
            time += 5
            previous = s[i]
        # remove screw
        time += 1
        # move to next screw
        if i != len(s) - 1:
         time +=1
    return time

print(sc('---+++'))