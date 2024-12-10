with open('input.txt', 'r') as f:
# with open('test.txt', 'r') as f:
    data = [int(c) for c in f.read().strip()]

d = {} # id -> (size, start_pos)
spaces = {} # pos -> size

i, j, id = 0, 0, 0 # i -> current pos in the data input; j -> current pos in the disk
while (i < len(data)):
    c, s = i, i+1

    if c < len(data): 
        d[id] = (data[c], j) # d[id] -> (size, start_pos)
        j += data[c] # update current pos in the disk
    if s < len(data): 
        if data[s] > 0: spaces[j] = data[s]
        j += data[s]

    id += 1
    i += 2 # move to the next file

for k, v in reversed(d.items()): # iterate over the files in reverse order
    size = v[0]
    for pos, space in sorted(spaces.items()): # find the first space that fits the file
        if pos >= v[1]: break
        if space >= size:
            d[k] = (d[k][0], pos) # update the start pos of the file
            if space - size > 0: spaces[pos + size] = space - size # update the space left after the file
            spaces.pop(pos) # remove the space that was used
            break

sol = 0
for k, v in d.items():
    n = v[0]
    pos = v[1]
    sol += k * (n * pos + n * (n - 1) // 2) # calculate the cost of the file

print(sol)
