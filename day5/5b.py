#!/usr/bin/python3a
from functools import cmp_to_key

rfile = open('rules.txt','r');
efile = open('examples.txt','r');

def custom_sort(rules):
    def compare(a, b):
        if b in rules[a]:
            return -1
        else:
            if a in rules[b]:
                return 1
            else:
                return 0
    return compare

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
    if not checkValid(ex,rules):
        ex_fixed = sorted(ex, key=cmp_to_key(custom_sort(rules)))
        result += ex_fixed[len(ex_fixed)//2]

print ('Result is: ' + str(result))


