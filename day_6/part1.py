def find_buff(chk_num):
    with open("input.txt", "r") as f1:
        count = chk_num
        charset = list(f1.read(chk_num))
        if (set(charset) != len(charset)):
            while True:
                charset.pop(0)
                charset.append(f1.read(1))
                count+=1
                
                if (len(set(charset)) != len(charset)):
                    continue
                else:
                    print(count)
                    break


find_buff(4)

