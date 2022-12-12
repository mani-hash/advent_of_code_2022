from crt_subroutine import sprite_check, draw, count_reset
cycle = 0
x = 1
width, height = 40, 6
count = 0

sprite = []
crt = [[] for i in range(height)]

with open("input.txt", "r") as f1:
    data = f1.read().splitlines()

sprite = sprite_check(x) #set starting sprite position

for i in data:
    if i == "noop":
        cycle += 1
        crt = draw(cycle, sprite, crt, count) #draw pixel per cycle
        count = count_reset(count) 

    elif "addx " in  i:
        v = int(i.replace("addx ", ""))
        cycle += 1
        crt = draw(cycle, sprite, crt, count) #draw pixel per cycle
        count = count_reset(count)
        cycle += 1
        crt = draw(cycle, sprite, crt, count) #draw pixel per cycle
        count = count_reset(count)
        x += v
        sprite = sprite_check(x)

for i in crt:
    for k in i:
        print(k, end="")
    print("")

