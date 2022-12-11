def check_head(H_pos, T_pos):
    tx = T_pos[0]
    ty = T_pos[1]
    hx = H_pos[0]
    hy = H_pos[1]
    # False: Tail doesn't move
    # True: Tail moves
    if (tx == hx) and (ty == hy):
        return False
    
    # length between co-ordinates
    elif (((tx - hx)**2 + (ty - hy)**2) == 1): # (parellel to x axis or y axis check)
        return False 
    else:
        if (((tx - hx)**2 + (ty - hy)**2) == 2): # (slanted gradient check)
            return False
        else:
            return True

def tail_move(H_pos, T_pos):
    tx = T_pos[0]
    ty = T_pos[1]
    hx = H_pos[0]
    hy = H_pos[1]

    if (tx == hx): #x axis are same (upwards or downward)
        if (hy > ty):
            return [tx, ty+1]
        else:
            return [tx, ty-1]

    elif (ty == hy): #y axis are same (left or right)
        if (hx > tx):
            return [tx+1, ty]
        else:
            return [tx-1, ty]
    else: 
        if (hx > tx): #right side
            
            if (hy > ty): 
                return [tx+1, ty+1]
            else:
                return [tx+1, ty-1]
        elif (hx < tx): #left side
            
            if (hy > ty):
                return [tx-1, ty+1]
            else:
                return [tx-1, ty-1]