#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

#array = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]

def snail(snail_map):
    turnPoint = snail_map[0][0]
    maxCounter = len(snail_map[0]) * len(snail_map[0])
    counter = 0
    xLoc = 0
    yLoc = 0
    snailPath = []
    snailMapTraveled = snail_map

    while counter < maxCounter - 1:
        if counter == 0:
            snailPath.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            xLoc += 1 
            counter += 1

        elif xLoc < len(snail_map[0])  and yLoc < len(snail_map) and counter < maxCounter - 2:
        #snailMapTraveled[yLoc][xLoc] != False:

            snailPath.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            xLoc += 1 
            counter += 1
            print(snailPath)
            print(counter)
            print(xLoc)
            print(yLoc)
        elif xLoc == len(snail_map) - 1 and yLoc < len(snail_map) and counter < maxCounter - 2:
            yLoc += 1
            snailPath.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            counter += 1
            print(snailPath)
            print(counter)
            print(xLoc)
            print(yLoc)
        
        elif xLoc > 0 and yLoc == len(snail_map) - 1 and counter < maxCounter - 2:
            xLoc -= 1
            snailPath.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            counter += 1
            print(snailPath)
            print(counter)
            print(xLoc)
            print(yLoc)

        elif xLoc == 0 and yLoc < 1 and counter < maxCounter - 2:
            yLoc -= 1
            snailPath.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            counter += 1
            print(snailPath)
            print(counter)
            print(xLoc)
            print(yLoc)
        
        else:
            xLoc += 1
            print(xLoc)
            snail_map.append(snail_map[yLoc][xLoc])
            snailMapTraveled[yLoc].pop(xLoc)
            snailMapTraveled[yLoc].insert(xLoc, False)
            counter += 1

    return snailPath

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))