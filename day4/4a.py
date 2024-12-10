#!/usr/bin/python3

file = open('input.txt','r');

result = 0
data = []
word = ["X","M","A","S"]

# Checks for word in a 2D matrix called data starting at position (i,j)
# Optionally only continues checking (recursivly) in a certain direction
def checkMatch(word,data,i,j,di=0,dj=0):
    
    prefix = '*' * (13-len(word))

    ## Main recusrsion guard
    ## If we've reached the end of the word, we've had a succesful match
    if len(word) == 0:
        print(prefix + "  Match found!")
        return 1
    
    ## Secondary guard
    ## If we reach the dge of the matrix, stop searching
    elif i < 0 or j < 0 or i >= len(data) or j >= len(data[0]):
        return 0
    
    else:
        
        #print(prefix + "Checking " +str(word)+ " at position ["+str(i)+","+str(j)+"] ("+data[i][j]+") in direction ["+str(di)+","+str(dj)+"]")
        ## Does the current letter match?
        if word[0] == data[i][j]:

            ## No direction yet? Check em all...
            if di == 0 and dj == 0:
                
                ## Recursivly check the 8 directions
                return (
                    checkMatch(word[1:],data, i,   j+1,  0,  1) +
                    checkMatch(word[1:],data, i,   j-1,  0, -1) +
                    checkMatch(word[1:],data, i-1, j-1, -1, -1) +
                    checkMatch(word[1:],data, i-1, j,   -1,  0) +
                    checkMatch(word[1:],data, i-1, j+1, -1,  1) +
                    checkMatch(word[1:],data, i+1, j-1,  1, -1) +
                    checkMatch(word[1:],data, i+1, j,    1,  0) +
                    checkMatch(word[1:],data, i+1, j+1,  1,  1)
                )
            else:
                ## Recursivly check the direction we are already going in
                return checkMatch(word[1:],data,i+di,j+dj,di,dj)
        
        ## letter doesnt' match?
        else:
            return 0


## Read Wordsearch into a big 2d array
for line in file:
    data.append(list(line.rstrip()));

## Ovierall dimensions of the wordsearch  (for bounds)
height = len(data)
width  = len(data[0])

## Go through the matrix looking for first letter
for i in range(0,height):
    for j in range(0,width):
        if data[i][j] == word[0]:
            
            ## if we find it, check to see how many copies of the word exist in any direction from this point
            result += checkMatch(word,data,i,j)

## Final total
print ('Result is: ' + str(result))

