from collections import defaultdict
import math

data = open('input.txt','r').read().split()
piles = defaultdict(int)

for n in data:
    piles[int(n)] = data.count(n)

for i in range(75):
    temp = defaultdict(int)

    for num,count in piles.items():
        if num == 0:
            temp[1] += count
        else:
            size = (math.floor(math.log10(num)) + 1)

            if size % 2 == 0:
                temp[ num // (10 ** (size // 2)) ] += count
                temp[ num %  (10 ** (size // 2)) ] += count
            else:
                temp[ num * 2024 ] += count

        piles = temp

print(str(sum(piles.values())))
