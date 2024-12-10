 #!/usr/bin/python3

##==============================================================================
## Generic helper functions for working with AdventOfCode Grid data
##
## We store grid data as an array of arrays e.g. grid[0][0] = top left value
##==============================================================================

## Converts a file into a grid, optionally, stored as ints
def populate_grid(file,dtype=''):
    grid_ds = []

    with open(file, 'r') as fh:
        for line in fh:
            if dtype == 'int':
                ## Store the value as an int
                grid_ds.append(list(map(int,line.strip())))
            else:
                ## Store it as a string (default)
                grid_ds.append(list(line.strip()))

    return grid_ds

##  Gets the height of a grid
def get_height (grid_ds):
    return len(grid_ds)

## gets the width of a grid
def get_width(grid_ds):
    return len(grid_ds[0])

## checks if a point (x,y) is outside the bounds of a grid
def out_of_bounds(x,y,grid_ds):
    if (0 <= x < get_width(grid_ds)) and (0 <= y < get_height(grid_ds)):
        return False
    else:
        return True

## Draw the current state of a grid - useful for debugging
def print_grid(grid_ds):
    for x in range(get_height(grid_ds)):
        for y in range(get_width(grid_ds)):
            print(grid_ds[x][y],end='')
        print()

##==============================================================================
## Problem specific functions from here on....
##==============================================================================

## Get the set of grid points (x,y) that contain the start number (0)
def get_trailheads(grid_ds):
    res = set()
    for x in range(get_height(grid_ds)):
        for y in range(get_width(grid_ds)):
            if grid_ds[x][y] == 0:
                res.add( (x,y) )
    return res


## Recursivly returns the number of complete paths from curr to target
## Also populate a set of the valid endpoints reached
def get_destinations(ci,cj,curr,target,values,destinations):

    ## either of these will break the recursion
    if out_of_bounds(ci,cj,values) or values[ci][cj] != curr:
        return 0

    if curr == target:
        ## We've completed a path! return a path (1) and store the endpoint
        destinations.add( (ci,cj) )
        return 1
    else:
        ## Otherwise, check the four neighbours (left, right, up, down)
        return (
                get_destinations(ci-1,cj,curr+1,target,values,destinations) +
                get_destinations(ci+1,cj,curr+1,target,values,destinations) +
                get_destinations(ci,cj-1,curr+1,target,values,destinations) +
                get_destinations(ci,cj+1,curr+1,target,values,destinations)
               )

##==============================================================================
## Main Code starts here
##==============================================================================

## Running totals
part_1_total = 0
part_2_total = 0

## Load the data into an array of arrays
values = populate_grid('input.txt','int')

## Iterate through every starting position
for (i,j) in get_trailheads(values):

    ## Temp totals for this trail head
    c_results = set()
    c_paths = 0

    ## Get the number of paths, and the set of destinations)
    c_paths = get_destinations(i,j,0,9,values,c_results)

    ## Update the totals
    part_1_total += len(c_results)
    part_2_total += c_paths

## All done, print the results
print(part_1_total,part_2_total)
