# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

def array_diff(a, b):
    remove = set(a)-set(b)
    item_list = [e for e in a if e in (list(remove))]
    return(item_list)
print(array_diff([1,2,2], [1])) 

# best solution
# def array_diff(a, b):
#    return [x for x in a if x not in b]