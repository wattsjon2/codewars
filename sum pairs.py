def sum_pairs(ints, s):
    index1 = 0
    index2 = 0
    storeindex1 = 0
    storeindex2 = 0
    while index1 < len(ints):
        while index2 < len(ints):
            if index1 == index2:
                index2 += 1
                pass
            if storeindex2 != 0 and index2 > storeindex2:
                break    
            if int(ints[index1]) + int(ints[index2]) == int(s):
                if storeindex1 == 0:
                    storeindex1 = index1
                    storeindex2 = index2
                    break
                else:
                    if storeindex2 > index2:
                        storeindex1 = index1
                        storeindex2 = index2
                    break               
            index2 += 1
        if storeindex2 != 0 and index1 >= storeindex2 -1:
            return[ints[storeindex1],ints[storeindex2]]
        index1 += 1
        index2 = 0 
        if index1 == len(ints) - 1 and storeindex2 == 0:
            return None 
    return[ints[storeindex1],ints[storeindex2]]

print(sum_pairs([4, -2, 3, 3, 4],8))

        