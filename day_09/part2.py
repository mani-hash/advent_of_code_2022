import ropeSys

x = 0
y = 0
head = "H"
tail = 9

pos = {
    "s": [x, y],
    head: [x, y]
}

for i in range(1, 10):
    pos[i] = [x, y]

# print(pos)

with open("input.txt", "r") as f1:
    data = f1.read().splitlines()
    data = [i.split() for i in data]

tail_pos = []

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

        if (ropeSys.check_head(pos[head], pos[1]) == True):
            pos[1] = ropeSys.tail_move(pos[head], pos[1])

        for m in range(1, 9):
            if (ropeSys.check_head(pos[m], pos[m+1]) == True):
                pos[m+1] = ropeSys.tail_move(pos[m], pos[m+1])

            if (m+1 == tail):
                tail_pos.append(pos[tail])

print(len(set(tuple(k) for k in tail_pos)))