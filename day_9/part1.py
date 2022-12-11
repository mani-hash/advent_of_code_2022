import ropeSys
head = "H"
tail = "T"
x = 0
y = 0

pos = {
    "s": [x, y],
    head: [x, y],
    tail: [x, y]
}

tail_pos = [] #store tail positions

with open("input.txt", "r") as f1:
    data = f1.read().splitlines()
    data = [i.split() for i in data]

for i in data:
    for k in range(0, int(i[1])):
        if (i[0] == "R"):
            pos[head][0] += 1
        elif (i[0] == "L"):
            pos[head][0] -= 1
        elif (i[0] == "U"):
            pos[head][1] += 1
        elif (i[0] == "D"):
            pos[head][1] -= 1

        if (ropeSys.check_head(pos[head], pos[tail]) == True):
            pos[tail] = ropeSys.tail_move(pos[head], pos[tail])

        tail_pos.append(pos[tail])


print(len(set(tuple(i) for i in tail_pos)))