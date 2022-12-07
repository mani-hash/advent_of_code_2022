import part1

t_disk = 70000000
space_need = 30000000
used_space = 0

direc = part1.dir

candidate = []
for x in direc:
    if (len(direc[x]["dir"]) != 0):
        value = part1.fold_sep(x, direc)
    else:
        value = direc[x]["size"]
    
    candidate.append(value)

candidate.sort(reverse=True)
used_space = candidate[0]
avail_space = t_disk - used_space

small = candidate[0]

for y in range(1, len(candidate)):
    if (avail_space + small >= space_need):
        if (avail_space + candidate[y]) < (avail_space + small):
            small = candidate[y]


# print(avail_space)
# print(candidate)
print(small)
