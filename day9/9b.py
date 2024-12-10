import copy

#with open("input_test.txt") as fin:
with open("input.txt") as fin:
    ## data ends up as an array of strings (each line)
    data = fin.read().strip().split("\n")

## Convert the line to an array according to prob spec
filenum = 0
data_unpacked = {}

#for 9b, store the data in chunks, rather than individual blocks
for i,val in enumerate(data[0]):
    if i % 2 == 0:
        ## Even: size of file
        data_unpacked[i] = [str(filenum) * int(val)]
        filenum += 1
    else:
        ## Odd: size of empty space
        data_unpacked[i] = ['.' * int(val) ]

print(data_unpacked)

def defrag(memory):

    j = len(memory) - 1

    while j > 0:
        ## if current chunk is a file
        if not '.' in memory[j]:

            ## go through the free spaces from the left
            for i in range(j):
                ## if theres a big enough free space
                if '.' in memory[i]  and len(memory[i]) >= len(memory[j]):
                    ## Break the free space up into a block for the file and whatevers left over
                    parta = [ '.' * len(memory[j]) ]
                    partb = [ '.' * (len(memory[i]) - len(memory[j])) ]

                    #print("Splitting into "+str(parta) +","+str(partb))
                    
                    ## do the swaps
                    #print("Swapping " +str(memory[j])+ " with " +str(parta))

                    memory[j],parta[0]= parta[0],memory[j]

                    if len(partb[0]) > 0:
                        memory = memory[:i] + parta + partb + memory[i+1:]
                        j += 1 
                    else:
                        memory = memory[:i] + parta + memory[i+1:]

                    break

            #print(memory)

        j -= 1


    #print(memory)

    ## Flatten the memeory 
    mem_flat = []
    for chunk in memory:
        for block in list(chunk):
            mem_flat.append(block)

    #print(mem_flat)

    ## Calc the mem score (according to prob spec):
    total = 0
    for i, val in enumerate(mem_flat):
        if val != '.':
            total += i * int(val)

    return(total)

mem = copy.deepcopy(data_unpacked)

#print(defrag(mem))
