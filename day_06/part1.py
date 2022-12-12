def find_buff(chk_num):
    with open("input.txt", "r") as f1:
        count = chk_num
        charset = list(f1.read(chk_num))
        while True:
            if (len(set(charset)) != len(charset)):
                charset.pop(0)
                charset.append(f1.read(1))
                count+=1
            else:
                print(count)
                break
            
find_buff(4)

