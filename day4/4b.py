#!/usr/bin/python3

file = open('input.txt','r');

result = 0
data = []

def checkXMAS(data,i,j):
    
    if i <= 0 or j <= 0 or i >= len(data)-1 or j >= len(data[0])-1:
        return 0
    
    diag1 = data[i-1][j-1] + data[i+1][j+1]
    diag2 = data[i-1][j+1] + data[i+1][j-1]
    
    if (diag1 == "MS"  or diag1 == "SM") and (diag2 == "MS"  or diag2 == "SM"):
        return 1
    else:
        return 0

for line in file:
    data.append(list(line.rstrip()));

for i in range(0,len(data)):
    for j in range(0,len(data[0])):
        if data[i][j] == 'A':
            result += checkXMAS(data,i,j)

print ('Result is: ' + str(result))


