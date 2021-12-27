def likes(names):
    like_string = ""
    if names == []:
        return('no one likes this')
    elif len(names) == 1:
        return(names[0] + " likes this")
    elif len(names) == 2:
        return(names[0] + " and " + names[1] + " like this")
    elif len(names) == 3:
        return(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    else:
        extra = len(names) - 2
        return(names[0] + ", " + names[1] + " and "  + str(extra) + " others like this") 



print(likes(['Ted', 'Phil', 'Bob']))

""" def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2) """