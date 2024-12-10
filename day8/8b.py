from collections import defaultdict
from itertools import combinations

with open("input.txt") as fin:
    ## data ends up as an array of strings (each line)
    data = fin.read().strip().split("\n")

## Get bounds of grid
height = len(data)
width  = len(data[0])

## Create an empty dict filled with empty arrays
## This will be our main data structure
## We dont store the entire grid - just coords of iteresting bits of the grid
locs = defaultdict(list)
for i in range(width):
    for j in range(height):
        if data[i][j] != ".":
            locs[data[i][j]].append((i, j))

## Get the antinodes for two locations tuples a (ax,ay), b (bx,by)
def get_antinodes(a,b,max_x,max_y):
    ax,ay = a
    bx,by = b

    ## Calc diff between the two points
    delta_x = bx - ax
    delta_y = by - ay

    ## Same as 8a, but now we loop to keep creating antinodes along the line
    for i in range(max_x):

        ##first antinode - take the diff away from point A
        cx = ax - (delta_x * i)
        cy = ay - (delta_y * i)

        if ( (0 <= cx < max_x) and (0 <= cy < max_y)):
            ## if its in bounds, add to result list    
            yield(cx,cy)

        ##second antinode - add the diff to point B
        dx = bx + (delta_x * i)
        dy = by + (delta_y * i)

        if ( (0 <= dx < max_x) and (0 <= dy < max_y)):
            ## if its in bounds, add to result list    
            yield(dx,dy)

## Set of all antinodes
results = set()

## Go through the data for each type of transmitter
for trans_type in locs:
    loc_list = locs[trans_type]

    print(loc_list)
    ## Get all valid pairs of locations in the list of locations for this transmitter type
    ## r=2 gets combinations of length 2 i.e. pairs
    for (trans_a,trans_b) in combinations(loc_list, r=2):

        print("checking "+str(trans_a) +","+str(trans_b))
        for antinode in get_antinodes(trans_a,trans_b,height,width):
            results.add(antinode)

## Print the final size of result set (num of antinodes)
print(len(results))
