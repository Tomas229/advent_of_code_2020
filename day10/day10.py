with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = int(input_file[i][0:-1])
    # print(input_file)


# 20:20
def count_jolt_diff(l):
    jolt1 = 0
    jolt3 = 1
    l.sort()
    res = 0 - l[0]
    if(res == -1):
        jolt1 += 1
    elif(res == -3):
        jolt3 += 1

    for i in range(len(l)-1):
        res = l[i]-l[i + 1]
        if(res == -1):
            jolt1 += 1
        elif(res == -3):
            jolt3 += 1
    return jolt1 * jolt3, l[len(l)-1] + 3


print(count_jolt_diff(input_file))


# primera parte 17 mins
input_file.sort()
input_file = [0]+input_file+[count_jolt_diff(input_file)[1]]
print(input_file)


def count_jolt_comb(l):
    res = l[1] - l[0]
    if(0 < res < 4):
        if(l[1] == 168):
            return 1
        return count_jolt_comb([l[0]]+l[2:]) + count_jolt_comb(l[1:])
    else:
        return 0


print(count_jolt_comb(input_file))
