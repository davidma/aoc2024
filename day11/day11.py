#!/usr/bin/python3
from collections import defaultdict

file = open('input.txt','r');

## Go through file, line by line
for line in file:

    ## split the line, map the chunks to ints, and make them into a list
    data = list(map(int, line.replace(':','').split()))

    ## Now, convert to a dict of number:count_stones
    ## Since the order of the stones doesn't matter, put them in piles
    ## We just have to keep track of the count of stones in each "pile"
    stones = defaultdict(int)
    for n in data:
        stones[n] = data.count(n)

    ## Number of blinks to simulate
    numblinks = 75

    for i in range(numblinks):

        ## New piles that will be made this iteration
        new_stones = defaultdict(int)

        for num,count in stones.items():

            # Rule 1: 0 pile all changes to 1
            if num == 0:
                new_stones[1] += count

            # Rule 2: any pile with even digits split into two
            # new piles, one for each new number
            elif len(str(num)) % 2 == 0:
                digits = str(num)
                size = len(digits) // 2
                num1 =  int(digits[:size])
                num2 =  int(digits[size:])

                new_stones[num1] += count
                new_stones[num2] += count

            # Rule 3: any remaining pile, multiply by 2024
            else:
                new_stones[num * 2024] += count

            ## replace the stones dict with the new one
            ## And go again...
            stones = new_stones

## Print the final result
## (Sum of the counts of stones in every pile)
print('Result is: ' + str(sum(stones.values())))
