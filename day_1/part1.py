f1 = open("input.txt", "r")

calories = 0
max_cal = 0

for line in f1:
    if (line == "\n"):
        if (calories > max_cal):
            max_cal = calories
        calories = 0
    else:
        calories += int(line.strip())

print(max_cal)


f1.close()