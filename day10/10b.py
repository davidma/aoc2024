#!/usr/bin/python3

with open("input.txt") as fin:
    ## data ends up as an array of strings (each line)
    data = fin.read().strip().split("\n")

## Get bounds of grid
height = len(data)
width  = len(data[0])

## Create an empty array which will be filled with arrays
## This will be our main data structure
values = []
trailheads = set()

for h in range(height):
    row = list(data[h])
    values.append([])
    for w in range(width):
        values[h].append(int(row[w]))
        if values[h][w] == 0:
            trailheads.add( (h,w) )

## Get the distinct number of paths taken (number of times we reach the target)
def get_paths(ci,cj,curr,target,values):
    if ci >= 0 and cj >= 0 and ci < len(values) and cj < len(values[0]):
        if values[ci][cj] == curr:
            ## We did it!
            if curr == target:
                return 1
            else:
                num = 0

                num += get_paths(ci-1,cj,curr+1,target,values)
                num += get_paths(ci+1,cj,curr+1,target,values)
                num += get_paths(ci,cj-1,curr+1,target,values)
                num += get_paths(ci,cj+1,curr+1,target,values)

                return num
        else: 
            return 0
    else:
        return 0

total = 0 

for (i,j) in trailheads:
    total += get_paths(i,j,0,9,values)

print(total)
