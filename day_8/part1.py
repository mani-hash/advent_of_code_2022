visible = 0

def check(inp, t_list, direc):
    check_set = t_list[inp][1:-1]
    if (direc == "right"):
        r_vis = [i for i in range(0, len(check_set))]
        for v in range(1, len(t_list[inp][:-1])): 
            for k in t_list[inp][v+1:]: 
                if (int(t_list[inp][v]) <= int(k)):
                    r_vis.pop(r_vis.index(v-1))
                    break
        return check(inp, t_list, "left") + r_vis
    elif (direc == "left"):
        l_vis = [i for i in range(0, len(check_set))]
        for v in range(1, len(t_list[inp][:-1])): 
            for k in t_list[inp][:v]: 
                if (int(t_list[inp][v]) <= int(k)):
                    l_vis.pop(l_vis.index(v-1))
                    break
            
        return check(inp, t_list, "up") + l_vis
    elif (direc == "up"):
        u_vis = [i for i in range(0, len(check_set))]
        for v in range(1, len(t_list[inp][:-1])): 
            for k in range(0, inp):
                
                if (int(t_list[inp][v]) <= int(t_list[k][v])):
                    u_vis.pop(u_vis.index(v-1))
                    break
        return check(inp, t_list, "down") + u_vis
    elif (direc == "down"):
        d_vis = [i for i in range(0, len(check_set))]
        for v in range(1, len(t_list[:-1])):       
            for k in range(1, len(t_list[inp:])):
                if (int(t_list[inp][v]) <= int(t_list[inp+k][v])):
                    d_vis.pop(d_vis.index(v-1))
                    break
        return d_vis

with open("input.txt", "r") as f1:
    trees = f1.read().splitlines()
    visible += ((len(trees[0]) + (len(trees))) * 2) - 4

for i in range(1, len(trees)-1):
    visible += len(set(check(i, trees, "right")))

print(visible)
    
    



    


