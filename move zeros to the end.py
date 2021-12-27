def move_zeros(array):
    zero_count = array.count(0)
    array.remove(0)
    for i in range(zero_count):
        array.append(0)
    return(array)

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))