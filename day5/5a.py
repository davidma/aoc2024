#!/usr/bin/python3

rfile = open('rules.txt','r');
efile = open('examples.txt','r');

def checkValid(ex, rules):
    for i in range(1,len(ex)):
        ## ex[i] must be in the ruleset for all preceeding values ex[:i] 
        for j in ex[:i]:
            if j in rules.keys():
                if not ex[i] in rules[j]:
                    return False
            else:
                return False

    ## still here, all good
    return True

result = 0
rules = {}
examples =[]

for line in rfile:
    (a,b) = list(map(int,line.rstrip().split('|')))

    if a in rules.keys():
        rules[a].append(b)
    else:
        rules[a] = [ b ]

for line in efile:
    examples.append(list(map(int,line.rstrip().split(','))))

for ex in examples:

    if checkValid(ex,rules):
        result += ex[len(ex)//2]

print ('Result is: ' + str(result))


