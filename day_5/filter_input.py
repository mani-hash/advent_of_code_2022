temp_stack = []
sub_stack = []
main_stack = []
commands = []

#get commands and unfiltered crate info
with open("input.txt", "r") as f1:
    stage = 0
    for line in f1:
        if (line == "\n"):
            stage += 1
            continue

        if (stage == 0):
            temp_stack.append(line.replace("\n", ""))
        else:
            commands.append(line.strip().replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
            # print(commands[0])


del temp_stack[-1]  #delete unnecesary part of list



start = 0
prog = 3
STEP = 4

# print(len(temp_stack))

#filter crates to useable manner
for i in range(0, 8):
    sub_stack.append([]) 
    for k in range(0, 9):
        # print(start, prog)
        sub_stack[i].append(temp_stack[i][start:prog].strip())
        # print(main_stack[int(i)-1])
        start += STEP
        prog += STEP
    prog = 3
    start = 0




#order crates in useable manner
for i in range (0, len(sub_stack[0])):
    main_stack.append([])
    for k in range(0, len(sub_stack)):
        if (sub_stack[k][i] != ""):
            main_stack[i].append(sub_stack[k][i].replace("[", "").replace("]", ""))