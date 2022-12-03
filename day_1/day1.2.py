f1 = open("input.txt", "r")

calories = 0
cal_arr = []
t = 0

for line in f1:
    if (line == "\n"):
        cal_arr.append(calories)
        calories = 0
    else:
        calories += int(line.strip())

cal_arr.sort(reverse=True)

for cal in cal_arr[:3]:
    t+= cal


print(t)



f1.close()