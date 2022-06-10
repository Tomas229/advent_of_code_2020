import copy
with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = input_file[i][0:-1]
    # print(input_file)


def solve(l):
    num = int(l[0])
    ships = [int(x) for x in l[1].split(",") if x != "x"]
    time = []
    for i in ships:
        if(num % i == 0):
            time += [0]
        else:
            time += [(int(num/i) + 1)*i - num]

    return min(time) * ships[time.index(min(time))]


print(solve(input_file))
# 27 mins


def solve2(l):
    ships = [[int(x), l[1].split(",").index(x)]
             for x in l[1].split(",") if x != "x"]

    numnum = ships[0][0]
    ships = ships[1:]
    i = numnum
    while(True):
        si = True
        for e in ships:
            if (i + e[1]) % e[0] != 0:
                si = False
                break
        if(si):
            return i
        i = i + numnum


print(solve2(["123", "17,x,13,19"]))
print(solve2(input_file))
# 30 mins
