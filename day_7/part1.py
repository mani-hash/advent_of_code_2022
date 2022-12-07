dir = {}
total = 0


def fold_sep(root, inp):
    cur_dir = inp[root]["dir"]
    total = 0
    for dir in cur_dir:
        if (len(inp[root + "," + dir]["dir"]) != 0):
            total += fold_sep(root + "," + dir, inp)
        total += inp[root + "," + dir]["size"]

    return total + inp[root]["size"]

        


with open("input.txt", "r") as f1:
    data = f1.read().splitlines()
    work_dir = ""
    store = 0
    for i in data:
        if ("$ cd .." in i):
            work_dir = work_dir[:work_dir.rfind(",")]
        
        elif ("$ cd " in i):
            work_dir += "," + i[5:]
            dir[work_dir] = {}
            dir[work_dir]["dir"] = []
            dir[work_dir]["size"] = 0
        elif ("$ ls" in i):
            store = 1
            
        
        else:
            if ("dir" in i):
                
                dir[work_dir]["dir"].append(i[4:])
            else:
                dir[work_dir]["size"] += int(i.split(" ")[0])


for x in dir:
    # print(x, "=>", dir[x])
    if (len(dir[x]["dir"]) != 0):
        value = fold_sep(x, dir)
    else:
        value = dir[x]["size"]
    if (value <= 100000):
        total+=value

if __name__ == "__main__":
    print(total)



