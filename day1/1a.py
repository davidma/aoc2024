import regex as re

file = open('input.txt','r');

result = 0

list_1 = []
list_2 = []

## Populate the lists
for line in file:
    (a,b) = line.split();
    list_1.append(int(a))
    list_2.append(int(b))
    
## Sort the lists
list_1.sort()
list_2.sort()

## Compare the two lists
for (index,item) in enumerate(list_1):
    distance =  abs(list_1[index] - list_2[index])
    result = result + distance

print ('Result is: ' + str(result))
