def maze_runner(maze):
    for a in maze:
        for i in a:
            if a.find(2) == True:
            y = a
            x = a.index(2)
            break

print(maze_runner([[1,1,1,1,1,1,1],
            [1,0,0,0,0,0,3],
            [1,0,1,0,1,0,1],
            [0,0,1,0,0,0,1],
            [1,0,1,0,1,0,1],
            [1,0,0,0,0,0,1],
            [1,2,1,0,1,0,1]]))