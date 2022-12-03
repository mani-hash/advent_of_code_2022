import re

priority = "abcdefghijklmnopqrstuvwxyz"
priority += priority.upper()

total = 0


with open("input.txt", "r") as f1:
    for line in f1:
        midpoint = len(line)//2
        comp1 = line[:midpoint]
        comp2 = line[midpoint:].strip()
        common = re.findall("[" + comp1 + "]", comp2)
        total += priority.index(common[0]) + 1

print(total)

