import copy

#with open("input_test.txt") as fin:
with open("input.txt") as fin:
    ## data ends up as an array of strings (each line)
    data = fin.read().strip().split("\n")

## Convert the line to an array according to prob spec
filenum = 0
data_unpacked = []

for i,val in enumerate(data[0]):
    for j in range(int(val)):
        if i % 2 == 0:
            ## Even: size of file
            data_unpacked.append(str(filenum))
        else:
            ## Odd: size of empty space
            data_unpacked.append('.')

    ##Increment filenum if it was an even iteration
    if  i % 2 == 0:
        filenum += 1

print(data_unpacked)

def defrag(memory):

    i = 0
    j = len(memory) - 1

    while i < j:
        if memory[i] == '.':
            ## free space found - get next data from end
            while memory[j] == '.':
                j -= 1
 
            ##print("Swapping data "+memory[j]+" at "+str(j)+" with free space at "+str(i))
            ## Swap the values
            memory[i],memory[j] =memory[j],memory[i]
    
        i += 1

    ## Calc the mem score (according to prob spec):
    total = 0
    for i, val in enumerate(memory):
        if val != '.':
            total += i * int(val)

    return(total)

mem = copy.deepcopy(data_unpacked)

print(defrag(mem))
