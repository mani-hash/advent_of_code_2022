count = 0
with open("input.txt", "r") as f1:
    for line in f1:
        pair = line.strip().split(",")
        pair[0] = pair[0].split("-")
        pair[1] = pair[1].split("-")
        list1 = [[], []]
        
        for i in range(0, 2):
            for k in range(int(pair[i][0]), int(pair[i][1]) + 1):
                list1[i].append(int(k))
            list1[i] = set(list1[i])

        
        if (bool(list1[0].intersection(list1[1]))):
            count+=1
        

print(count)