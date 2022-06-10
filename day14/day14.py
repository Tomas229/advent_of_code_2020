with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


def solve(l):
    mask = l[0][7:]
    l = l[1:]
    mem = dict()
    for i in l:
        i = i.split("=")
        if i[0] == "mask ":
            mask = i[1][1:]
            continue
        num = int(i[1])
        entry = int(i[0][4:-2])
        mem[entry] = masked(mask, num)
    sum = 0
    for i in mem:
        sum += mem[i]
    return sum


def masked(mask, num):
    mask = list(mask)
    mask.reverse()
    num = list(bin(num))[2:]
    num.reverse()
    for i in range(len(num)):
        if mask[i] == "X":
            mask[i] = num[i]
    mask.reverse()
    mask = "".join(mask).replace("X", "0")
    return int(mask, 2)


print(solve(["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
             "mem[8] = 11",
             "mem[7] = 101",
             "mem[8] = 0"]))
print(solve(input_file))

# 50 mins parte 1
