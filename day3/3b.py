#!/usr/bin/python3
import regex as re

file = open('input.txt','r');

result = 0
state  = True

def getRealMuls(input_txt,state):
  
    pattern1 = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"    ## Regex to match the correct mul(a,b) substrings, plus do() and don't()
    pattern2 = "[0-9]+"                                   ## Regex to match the numbers insidee the mul substring
    total = 0

    for value in re.findall(pattern1,input_txt):

        print(value)

        if  value == "do()":
            state = True

        elif value == "don't()":
            state = False

        else:
            if state:
                (a,b) = list(map(int,re.findall(pattern2,value)))
                print("adding")
                total += a*b
    
    return total,state

for line in file:
    (linetotal,state) = getRealMuls(line,state)

    result += linetotal
    
print ('Result is: ' + str(result))
