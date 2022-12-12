from crt_subroutine import list_chk
cycle = 0
x = 1
total = 0

with open("input.txt", "r") as f1:
    data = f1.read().splitlines()

for i in data:
    if i == "noop":
        cycle += 1
        total += list_chk(cycle, x)
    elif "addx " in  i:
        v = int(i.replace("addx ", ""))
        cycle += 1
        total += list_chk(cycle, x)
        cycle += 1
        total += list_chk(cycle, x)
        x += v

print(total)