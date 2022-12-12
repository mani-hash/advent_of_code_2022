high_score = []

def check(inp, t_list, direc, score_dict):
    if (direc == "right"):
        for v in range(1, len(t_list[inp][:-1])): 
            count = 0
            for k in t_list[inp][v+1:]: 
                count+=1
                if (int(t_list[inp][v]) <= int(k)):  
                    break
            score_dict[v] *= count

        return check(inp, t_list, "left", score_dict)

    elif (direc == "left"):
        for v in range(1, len(t_list[inp][:-1])): 
            count=0
            for k in reversed(t_list[inp][:v]): 
                count+=1
                if (int(t_list[inp][v]) <= int(k)):                   
                    break
            score_dict[v] *= count
        return check(inp, t_list, "up", score_dict) 
    elif (direc == "up"):
        for v in range(1, len(t_list[inp][:-1])): 
            count = 0
            for k in range(inp-1, -1, -1):
                count += 1
                if (int(t_list[inp][v]) <= int(t_list[k][v])):
                    break
            score_dict[v] *= count

        return check(inp, t_list, "down", score_dict)

    elif (direc == "down"):
       
        for v in range(1, len(t_list[:-1])):
            count = 0
            for k in range(1, len(t_list[inp:])):
                count += 1
                if (int(t_list[inp][v]) <= int(t_list[inp+k][v])):
                    
                    
                    break
            score_dict[v] *= count

        return score_dict

with open("input.txt", "r") as f1:
    trees = f1.read().splitlines()


for i in range(1, len(trees)-1):
    scenic_score = { i: i-(i-1) for i in range(1, len(trees[i][:-1])) }
    score = check(i, trees, "right", scenic_score)
    high = 0
    for key in score:
        if (score[key] > high):
            high = score[key]

    high_score.append(high)

print(max(high_score))

    
    



    


  
    

