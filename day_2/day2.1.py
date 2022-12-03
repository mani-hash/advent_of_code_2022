choice = {"col1": {"A": 1, "B": 2, "C": 3}}

compet = {"X": 0, "Y": 3, "Z": 6}

def choose(op, option):
    if (option == "Y"):
        return op
    elif (option == "Z"):
        if (op < 3):
            return op + 1
        else:
            return 1
    elif (option == "X"):
        if (op > 1):
            return op - 1
        else:
            return 3


total = 0

with open("input.txt", "r") as f1:
    for line in f1:
        output = line.strip().split(" ")
        
        point = choose(choice["col1"][output[0]], output[1])
        total += point
        total += compet[output[1]]

print(total)



