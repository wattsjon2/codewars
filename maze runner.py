def maze_runner(maze, directions):
    y = 0
    ycheck = 0
    x = 0
    for i in maze:
        xcheck = 0
        for j in i:
            if j == 2:
                x = xcheck
                y = ycheck
            xcheck += 1
        ycheck += 1
    
    for dir in directions:
        if dir == 'N':
            y -= 1
        elif dir == 'S':
            y += 1
        elif dir == 'E':
            x += 1
        elif dir == 'W':
            x -= 1
        if y > len(maze) - 1 or x > len(maze[0]) - 1:
            return('Dead')
        if maze[y][x] == 1:
            return('Dead')
        if maze[y][x] == 3:
            return('Finish')        
    return('Lost') 
print(maze_runner([
[1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 3], 
[1, 0, 1, 0, 1, 0, 1], 
[0, 0, 1, 0, 0, 0, 1], 
[1, 0, 1, 0, 1, 0, 1], 
[1, 0, 0, 0, 0, 0, 1], 
[1, 2, 1, 0, 1, 0, 1]], ['N', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'S']))