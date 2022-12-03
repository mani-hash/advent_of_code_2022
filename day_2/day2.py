choice = {"col1": {"A": 1, "B": 2, "C": 3}, "col2": {"X": 1, "Y": 2, "Z": 3}}

compet = {"lost": 0, "draw": 3, "won": 6}

def defeat(op, you):
    if (op == you):
        return "draw"
    elif ((op == you + 2) or (you == op + 1)):
        return "won"
    elif ((op == you + 1) or (you == op + 2)):
        return "lost"




total = 0

with open("input.txt", "r") as f1:
    for line in f1:
        output = line.strip().split(" ")
        
        status = defeat(choice["col1"][output[0]], choice["col2"][output[1]])
        total += compet[status]
        total += choice["col2"][output[1]]

print(total)



