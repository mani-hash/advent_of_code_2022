import filter_input as fil

crates = fil.main_stack #contains filtered input as a 2D list
orders = fil.commands #contains the Elf instructions as 2-D list (no of box, source column, destination column)

for num in orders:
    for x in range(int(num[0]) - 1, -1, -1):
        crates[int(num[2]) - 1].insert(0, crates[int(num[1]) - 1][x])
        del(crates[int(num[1]) - 1][x])

for i in crates:
    print(i[0], end="")


 
        
