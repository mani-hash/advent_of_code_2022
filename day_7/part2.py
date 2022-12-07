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
max_space = t_disk - space_need


free = 0

for i in range(1, len(candidate)):
    if (used_space - candidate[i] <= max_space):
        free = candidate[i]



print(free)



