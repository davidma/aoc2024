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
i =  0

while i < len(list_1):
    similarity = list_1[i] * list_2.count(list_1[i])
    result = result + similarity

    i = i + 1

print ('Result is: ' + str(result))
