import regex as re

file = open('input.txt','r');

result = 0

## takes a list of ints, checks if its safe
## Safe = all increasing or all decreasing (no mix) and all diffs between 1 and 3
def isSafe(list):

    diffs = []

    ## Get a list of the diffs between all pairs in the list
    for i in range(1,len(list)):
        diffs.append(list[i] - list[i-1])

    ## Check if its safe by either definition
    good_asc = all( 1 <= x <=  3 for x in diffs) # All diffs positive, and between 1 and 3
    good_dec = all(-3 <= x <= -1 for x in diffs) # All diffs negative, and between 1 and 3

    ## Return true if either was true
    return good_asc or good_dec 


## Go through file, line by line
for line in file:
   
    ## split the line, map the chunks to ints, and make them into a list
    numbers = list(map(int, line.split()))

    ## check if the line is safe or not
    if isSafe(numbers):
        result = result + 1
    
## Print the final result
print ('Result is: ' + str(result))
