def list_chk(a, b):
    cycle_list = [20, 60, 100, 140, 180, 220]
    if (a in cycle_list):
        return a*b
    else:
        return 0

def count_reset(count):
    count+= 1
    if count > 39:
        return 0
    return count

def draw(pos, sprite, crt, count):
    dic1 ={1:range(1, 41), 2:range(41, 81), 3:range(81, 121), 4:range(121, 161), 5:range(161, 201), 6:range(201, 241)}
    for key in dic1:
        if pos in dic1[key]:
            if sprite[count] == "#":
                crt[key-1].append("#")
                return crt
            else:
                crt[key-1].append(".")
                return crt

def sprite_check(inp):
    char = ["." for i in range(40)]
    if (inp > -1):
        char[inp] = "#"
    if (inp > 0):
        char[inp-1] = "#"
    if inp < 39:
        char[inp+1] = "#"
    return char