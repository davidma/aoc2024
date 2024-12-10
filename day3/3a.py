#!/usr/bin/python3
import regex as re
import math

file = open('input.txt','r');

result = 0

## Returns the sum of the real mul(a,b) operations in a given line of text
def getRealMuls(input_txt):
  
    pattern1 = 'mul\([0-9]+\,[0-9]+\)'  ## Regex to match the correct mul(a,b) substrings
    pattern2 = '[0-9]+'                 ## Regex to match the numbers insidee the mul substring
    total = 0              

    ## Find all matches for pattern1, iterate through them
    for realMul in re.finditer(pattern1,input_txt):

        #for each one, make a list of the actual numbers
        numbers = list(map(int,re.findall(pattern2,realMul[0])))

        ## multiply them together, add to total
        total += math.prod(numbers)
    
    return total


## Go through file, line by line
for line in file:
    result += getRealMuls(line)
    
## Print the final result
print ('Result is: ' + str(result))
