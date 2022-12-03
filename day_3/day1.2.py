import re

priority = "abcdefghijklmnopqrstuvwxyz"
priority += priority.upper()

total = 0
group_list = []

with open("input.txt", "r") as f1:
    for line in f1:
        group_list.append(line.strip())

        if (len(group_list) == 3):
            for val in group_list[0]:
                if ((val in group_list[1]) and (val in group_list[2])):
                    repeated = val
                    
            total += priority.index(repeated) + 1


            group_list = []        

print(total)

