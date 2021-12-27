#return the sum of all numbers divisible by 3 or 5 below the given number

def solution(number):
    storenum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            storenum += i
    return(storenum)
    
print(solution(6))

#def solution(number):
#    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)