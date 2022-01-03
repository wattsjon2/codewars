#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

#array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]

def snail(snail_map):
    snailPath = []
    direction = 'right'

    while snail_map != []:

        if snail_map[0] == [] and direction == 'right':
            direction = 'down'
            downCount = 0
            snail_map.pop(0)
        
        elif direction == 'down' and downCount == len(snail_map):
            direction = 'left'
            downCount -= 1


        elif direction == 'left' and snail_map[downCount] == []:
            direction = 'up'
            snail_map.pop(downCount)
            downCount -= 1

        elif direction == 'up' and downCount == -1:
            direction = 'right' 
            downCount = 0
 
            
        elif direction == 'right':
            snailPath.append(snail_map[0].pop(0))
        
        elif direction == 'down' and downCount < len(snail_map):
            snailPath.append(snail_map[downCount].pop(-1))
            downCount += 1
        
        elif direction == 'left' and snail_map[downCount] != []:
            snailPath.append(snail_map[downCount].pop(-1)) 

        elif direction == 'up' and downCount != -1:
            snailPath.append(snail_map[downCount].pop(0))
            downCount -= 1
        
    return snailPath

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
array2 = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]
array3 = [[1,2,3],
         [8,9,4],
         [7,6,5]]

print(snail(array))
print(snail(array2))
print(snail(array3))