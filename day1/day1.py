def two_sum(lista, num):  # O(n^2)
    num_1 = 1
    num_2 = 1
    count = 0

    for i in lista:
        for j in lista:
            count += 1
            if (i + j == num):
                num_1 = i
                num_2 = j
                break

    return num_1*num_2


def two_sum_new(lista, num):
    num_1 = 1
    num_2 = 1
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
            num_1 = lista[l]
            num_2 = lista[r]
            break

    return num_1*num_2  # O(nlog n)


def three_sum(lista, num):
    num_1 = 1
    num_2 = 1
    num_3 = 1
    count = 0

    for i in lista:
        for j in lista:
            for k in lista:
                count += 1
                if (i + j + k == num):
                    num_1 = i
                    num_2 = j
                    num_3 = k
                    break

    return num_1*num_2*num_3


def three_sum_new(lista, num):
    num_1 = 1
    num_2 = 1
    lista.sort()  # O(nlogn)

    for i in lista:
        res = two_sum_new(lista, num-i)  # O(nlogn)
        if(res != 1):
            num_1 = res
            num_2 = i
            break

    return num_1*num_2


with open("input.txt") as file:
    pass_file = file.readlines()
    for i in range(len(pass_file)):
        pass_file[i] = pass_file[i][0:-1]
        pass_file[i] = int(pass_file[i])

    print(two_sum_new(pass_file, 2020))
    print(three_sum_new(pass_file, 2020))
