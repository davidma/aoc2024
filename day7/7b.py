#!/usr/bin/python3
import math

file = open('input.txt','r');

result = 0

def concat(a,b):
    return int(f"{a}{b}")

## takes a list of ints, and a target value
## checks if the target can be reached by combining the numbers with + and * operators
def isCalculable(target,total,numlist):
    if len(numlist) == 0:
        if total == target:
            return True
        else:
            return False
    else:
        return (
                isCalculable(target,total * numlist[0], numlist[1:]) or
                isCalculable(target,total + numlist[0], numlist[1:]) or
                isCalculable(target,concat(total,numlist[0]), numlist[1:])
               )

## Go through file, line by line
for line in file:
   
    ## split the line, map the chunks to ints, and make them into a list
    numbers = list(map(int, line.replace(':','').split()))

    ## check if the line is safe or not
    if isCalculable(numbers[0], numbers[1], numbers[2:]):
        result = result + numbers[0]
    
## Print the final result
print ('Result is: ' + str(result))
