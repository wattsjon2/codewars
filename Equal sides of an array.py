#You are going to be given an array of integers. Your job is to take that array and find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index that would make this happen, return -1.

def find_even_index(arr):
    index = 0
    while index < len(arr):
        left = sum(arr[:index])
        right = sum(arr[index + 1:])
        if left == right:
            return index
        elif index == len(arr) - 1:
            return -1
        else:
            index +=1

print(find_even_index([1,100]))

# best solution

#def find_even_index(arr):
#    for i in range(len(arr)):
#        if sum(arr[:i]) == sum(arr[i+1:]):
#            return i
#    return -1
