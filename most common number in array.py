def highest_rank(arr):
    count = 0
    num_store = 0
    for i in arr:
        if arr.count(i) >= count and i != num_store:
            if arr.count(i) == count and i > num_store:
                count = arr.count(i)
                num_store = i
            elif arr.count(i) > count:
                count = arr.count(i)
                num_store = i
    return num_store

print(highest_rank([1,2,3,4,5,6,7,0]))


#

#def highest_rank(arr):
#    if arr:
#        c = Counter(arr)
#        m = max(c.values())
#        return max(k for k,v in c.items() if v==m)


#def highest_rank(arr):
#    return max(sorted(arr,reverse=True), key=arr.count)