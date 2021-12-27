# remove zeros from a list and move them to the end
def move_zeros(array):
    zero_count = array.count(0)
    for i in range(zero_count):
        array.remove(0)
    for i in range(zero_count):
        array.append(0)
    return(array)

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))


""" 
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l)) 
    """