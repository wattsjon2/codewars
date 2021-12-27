# Remove directions that immediatly cancel each other out

def dirReduc(arr):
    a = 0
    while a < len(arr):
        if a == len(arr) - 1:
            break 
        if arr[a] == "EAST" and arr[a+1] == "WEST":
            del arr[a:a+2]
            a = 0
        elif arr[a] == "WEST" and arr[a+1] == "EAST":
            del arr[a:a+2]
            a = 0
        elif arr[a] == "NORTH" and arr[a+1] == "SOUTH":
            del arr[a:a+2]
            a = 0
        elif arr[a] == "SOUTH" and arr[a+1] == "NORTH":
            del arr[a:a+2]
            a = 0
        else:
            a += 1
    return(arr)

print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

def dirReduc2(arr):
    opposites = [{'NORTH', 'SOUTH'}, {'EAST', 'WEST'}]
    
    for i in range(len(arr)-1):
        if set(arr[i:i+2]) in opposites:
            del arr[i:i+2]
            return dirReduc(arr)
    
    return arr 