with open("input.txt") as file:
    input_file = file.readlines()
    for i in range(len(input_file)):
        input_file[i] = int(input_file[i][0:-1])
    # print(input_file)


def two_sum_new(lista, num):
    num_1 = -1
    lista.sort()  # O(nlogn)

    l = 0
    r = len(lista) - 1
    while (l < r):
        num_i = lista[l] + lista[r]
        if(num_i < num):
            l += 1
        elif(num_i > num):
            r -= 1
        elif(num_i == num):
            num_1 = num
            break

    return num_1  # O(nlog n)


# 30 min
def decode(l, a):
    index_1 = 0
    index_2 = a
    while(two_sum_new(l[index_1:index_2], l[index_2]) == l[index_2]):
        index_1 += 1
        index_2 += 1
    return l[index_2]


decode([35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576], 5)
print(decode(input_file, 25))


def decode_2(l, a):
    num = decode(l, a)
    index_1 = 0
    index_2 = 2
    while (sum(l[index_1:index_2]) != num):
        aux = sum(l[index_1:index_2])
        if(aux < num):
            index_2 += 1
        elif(aux > num):
            index_1 += 1

    return max(l[index_1:index_2])+min(l[index_1:index_2])


print(decode_2(input_file, 25))
# 12 mins
