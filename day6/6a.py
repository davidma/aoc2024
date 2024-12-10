#!/usr/bin/python3
import copy

file = open('input.txt','r');

## Empty maze
maze = []

## Guard cycles through these coord transforms by turning right
directions = { 
               0 : (  0, -1),  ## Up, Aka North
               1 : (  1,  0),  ## Right, Aka East
               2 : (  0,  1),  ## Down, Aka South
               3 : ( -1,  0)   ## Left, Aka West
             }

def drawMaze(cmaze,c_x,c_y):
    for i in range(0,len(cmaze)):
        for j in range(0,len(cmaze[0])):
            if j == c_x and i == c_y:
                print('$',end='')
            elif cmaze[j][i][1] == 1:
                print('X',end='')
            else:
                print(cmaze[j][i][0],end='')
        print()

def getPath(lmaze, c_x, c_y, c_d):
    while True:
        lmaze[c_x][c_y][1] = 1
        lmaze[c_x][c_y][2] = c_d

        n_x = c_x + directions[c_d][0]
        n_y = c_y + directions[c_d][1]

        if n_x == len(lmaze) or n_y  == len(lmaze[0]) or n_x < 0 or n_y < 0:
            break

        elif lmaze[n_x][n_y][0] == '#':
            c_d = (c_d + 1) % 4
        else:
            c_x = n_x
            c_y = n_y

    lpath = set()

    for i in range(0,len(lmaze)):
        for j in range(0,len(lmaze[0])):
            if lmaze[i][j][1] == 1:
                lpath.add((i,j))

    return lpath

def checkLoopExists(lmaze, c_x, c_y, c_d):

    i=0
    while i < 20000:

        #print (c_x,c_y,c_d,lmaze[c_x][c_y])

        if lmaze[c_x][c_y][1] == 1 and lmaze[c_x][c_y][2] == c_d:
            ##we've been here! loop
            #print("loop detected")
            return True

        lmaze[c_x][c_y][1] = 1
        lmaze[c_x][c_y][2] = c_d
        n_x = c_x + directions[c_d][0]
        n_y = c_y + directions[c_d][1]

        if n_x == len(lmaze) or n_y  == len(lmaze[0]) or n_x < 0 or n_y < 0:
            break

        elif lmaze[n_x][n_y][0] == '#':
            c_d = (c_d + 1) % 4
        else:
            c_x = n_x
            c_y = n_y

        i += 1

    return False


def checkNewObsticles(lmaze,c_x,c_y,c_d,lpath):

    ## Remove the starting point
    lpath.remove((c_x,c_y))

    count = 0

    for index,point in enumerate(lpath):

        #print(str(index) + " -> Trying new obsticle at "+str(point))

        x_to_change = point[0]
        y_to_change = point[1]

        cmaze = copy.deepcopy(lmaze)
        cmaze[x_to_change][y_to_change] = [ '#', 0, -1 ]

        if checkLoopExists(cmaze, c_x, c_y, c_d):
            count += 1

    return count

## Read Maze into a big 2d array
for line in file:
    row = list(line.rstrip())
    if len(maze) == 0:
        for i in range(len(row)):
            maze.append([])
    for i in range(0,len(row)):
        maze[i].append( [row[i], 0, -1])

# Go through the matrix looking for starting position
for i in range(0,len(maze)):
    for j in range(0,len(maze[0])):
        if maze[i][j][0] == '^':
            curr_x = i
            curr_y = j
            curr_d = 0
            maze[curr_x][curr_y][1] = 1

fresh_maze = copy.deepcopy(maze)

# Solve the maze, return the path taken and the annotated maze
path = getPath(maze,curr_x,curr_y,curr_d)
print ('P1 Result is: ' + str(len(path)))

# Brute force the number of changes that cause loops
numLoops = checkNewObsticles(fresh_maze,curr_x,curr_y,curr_d,path)
print  ('P2 Result is: ' + str(numLoops))
